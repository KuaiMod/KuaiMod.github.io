import json
import numpy as np
from collections import defaultdict
import argparse

# 类别到索引的映射
label_to_idx = {
    '正向': 0, '违法犯罪': 1, '涉政不当言行': 2, '辱骂、引战、宣扬仇恨': 3, '出售违禁品': 4,
    '历史虚无主义': 5, '色情低俗': 6, '不实信息': 7, '危害未成年人身心健康': 8,
    '未成年不适当行为': 9, '夸大商品功效': 10, '引导私下交易': 11, '虚假承诺福利': 12,
    '炒作卖货': 13, '未添加AI标识': 14, '盗用抄袭作品': 15
}

CATEGORY_MAPPING = {
    "法律与社会安全": ["违法犯罪", "涉政不当言行", "辱骂、引战、宣扬仇恨", "出售违禁品", "历史虚无主义"],
    "内容质量与伦理": ["色情低俗", "不实信息", "危害未成年人身心健康", "未成年不适当行为"],
    "商业行为与商品宣传": ["夸大商品功效", "引导私下交易", "虚假承诺福利", "炒作卖货"],
    "知识产权与标识合规": ["未添加AI标识", "盗用抄袭作品"],
    "正向": ["正向"]
}

SECOND_TO_FIRST = {sub_tag: main_tag for main_tag, sub_tags in CATEGORY_MAPPING.items() for sub_tag in sub_tags}

def main(file_path):
    # 统计变量
    true_labels = []
    pred_labels = []
    category_recall = defaultdict(lambda: {'tp': 0, 'fn': 0})

    # 读取并处理JSONL文件
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)  
            ground_truth_tag = data['tag']
            predicted_response = data['judgement']

            # 预测标签
            predicted_tag = None
            for tag in label_to_idx.keys():
                if tag in predicted_response:
                    predicted_tag = tag
                    break
            if predicted_tag is None:
                continue

            # 二分类标签（0: 正向, 1: 非正向）
            y_true = 0 if ground_truth_tag == '正向' else 1
            y_pred = 0 if predicted_tag == '正向' else 1
            true_labels.append(y_true)
            pred_labels.append(y_pred)

            # 统计一级类别 recall
            first_level_label = SECOND_TO_FIRST[ground_truth_tag]
            if y_true == 1:  # 只计算非正向类别
                if y_pred == 1:
                    category_recall[first_level_label]['tp'] += 1
                else:
                    category_recall[first_level_label]['fn'] += 1

    # 计算二分类 accuracy
    true_labels = np.array(true_labels)
    pred_labels = np.array(pred_labels)
    accuracy = np.mean(true_labels == pred_labels)

    # 计算正向（0类）与非正向（1类）的 Precision 和 Recall
    tp_positive = np.sum((pred_labels == 0) & (true_labels == 0))
    fp_positive = np.sum((pred_labels == 0) & (true_labels == 1))
    tn_negative = np.sum((pred_labels == 1) & (true_labels == 1))
    fn_negative = np.sum((pred_labels == 1) & (true_labels == 0))

    positive_precision = tp_positive / max(1, tp_positive + fp_positive)
    positive_recall = tp_positive / max(1, tp_positive + fn_negative)
    negative_precision = tn_negative / max(1, tn_negative + fn_negative)
    negative_recall = tn_negative / max(1, tn_negative + fp_positive)

    # 计算每个一级类别的 recall
    category_recall_results = {cat: vals['tp'] / max(1, vals['tp'] + vals['fn']) for cat, vals in category_recall.items()}

    # 输出结果
    print(f"二分类 Accuracy: {accuracy:.4f}")
    print(f"正向 Precision: {positive_precision:.4f}")
    print(f"正向 Recall: {positive_recall:.4f}")
    print(f"非正向 Precision: {negative_precision:.4f}")
    print(f"非正向 Recall: {negative_recall:.4f}")
    print("各一级类别的 Recall:")
    for category, rec in category_recall_results.items():
        print(category_recall[category])
        print(f"{category}: {rec:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSONL file for classification metrics.')
    parser.add_argument('--input_file', type=str, help='Path to the JSONL file')
    args = parser.parse_args()
    main(args.input_file)