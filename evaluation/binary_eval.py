import json
from collections import defaultdict
from sklearn.metrics import accuracy_score, precision_score, recall_score
import argparse

# 一级类目和二级类目映射
CATEGORY_MAPPING = {
    "法律与社会安全": ["违法犯罪", "涉政不当言行", "辱骂、引战、宣扬仇恨", "出售违禁品", "历史虚无主义"],
    "内容质量与伦理": ["色情低俗", "不实信息", "危害未成年人身心健康", "未成年不适当行为"],
    "商业行为与商品宣传": ["夸大商品功效", "引导私下交易", "虚假承诺福利", "炒作卖货"],
    "知识产权与标识合规": ["未添加AI标识", "盗用抄袭作品"],
}

# 反向映射二级类目到一级类目
SECOND_TO_FIRST = {sub: cat for cat, subs in CATEGORY_MAPPING.items() for sub in subs}

def main(file_path):
    # 读取数据
    true_labels, pred_labels = [], []
    category_correct = defaultdict(int)
    category_total = defaultdict(int)

    # 统计每个一级类目的召回率数据
    first_category_stats = defaultdict(lambda: {'TP': 0, 'FN': 0})

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            tag = data['tag']
            pred = data['judgement']

            # 假设二分类任务中，标签为'否'表示负类，'是'表示正类
            true_label = '否' if tag != "正向" else '是'  # 这里需根据实际数据修改判断条件
            pred_label = pred

            true_labels.append(1 if true_label == '是' else 0)
            pred_labels.append(1 if pred_label == '是' else 0)

            # 统计一级类目
            first_category = SECOND_TO_FIRST.get(tag, None)
            if first_category:
                if true_label == '否':  # 负类样本
                    category_total[first_category] += 1
                    if pred_label == '否':  # 正确分类
                        category_correct[first_category] += 1
                    # 召回率相关统计
                    if '否' in pred_label and true_label == '否':
                        first_category_stats[first_category]['TP'] += 1
                    elif pred_label == '是' and true_label == '否':
                        first_category_stats[first_category]['FN'] += 1
                else:
                    print(pred_label)
            else:
                if tag != "正向":
                    print(data)

    # 计算整体指标
    accuracy = accuracy_score(true_labels, pred_labels)

    # 计算标签为'是'和'否'的Precision和Recall
    precision_yes = precision_score(true_labels, pred_labels, pos_label=1)
    recall_yes = recall_score(true_labels, pred_labels, pos_label=1)

    precision_no = precision_score(true_labels, pred_labels, pos_label=0)
    recall_no = recall_score(true_labels, pred_labels, pos_label=0)

    # 输出整体指标
    print(f"Overall Accuracy: {accuracy:.4f}")
    print(f"Precision for '是': {precision_yes:.4f}")
    print(f"Recall for '是': {recall_yes:.4f}")
    print(f"Precision for '否': {precision_no:.4f}")
    print(f"Recall for '否': {recall_no:.4f}")

    # 输出每个一级类目的召回率
    print("\nRecall for each First-Level Category:")
    for category, stats in first_category_stats.items():
        tp = stats['TP']
        fn = stats['FN']
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        print(f"{category}: Recall = {recall:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSONL file for classification metrics.')
    parser.add_argument('--input_file', type=str, help='Path to the JSONL file')
    args = parser.parse_args()
    main(args.input_file)