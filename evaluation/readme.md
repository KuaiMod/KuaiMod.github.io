# Benchmark Description

## Data Format

This dataset consists of multiple samples, each containing the following fields:

- `tag`: The label of the sample, indicating the category of the content, such as "pornographic".
- `title`: The title of the video, usually containing the username and user ID.
- `OCR`: Optical Character Recognition results, extracted text from images.
- `ASR`: Automatic Speech Recognition results, extracted text from audio.
- `images`: A list of image filenames, representing the cover and up to 8 frames extracted from the video.
- `pid`: A unique identifier for the sample.

## Example

```json
{
  "tag": "pornographic",
  "title": "@AUsername (A's ID)",
  "OCR": "Au|99. ELLYWTT|199. E|990. L|990. |199|199",
  "ASR": "it's good it summy bod night i'm good good you. |you want to number one.",
  "images": ["002_0.jpg", "002_1.jpg", "002_2.jpg", "002_3.jpg", "002_4.jpg", "002_5.jpg", "002_6.jpg", "002_7.jpg", "002_8.jpg"],
  "pid": "002"
}
```

# Evaluation Method

We provide evaluation scripts in our GitHub repository for text-based violation judgments.

The evaluation process involves storing the textual judgment results in a JSONL file. Each line is a dictionary containing the following keys:

- `tag`: The ground truth label of the instance.
- `judgement`: The response from the model or algorithm.
  - For Binary classification, the judgement for each video should be `是` (positive)  or `否`  (violative).
  - For Multi-Class classification, the judgement for each video should be one of 17 tags.
## **Evaluation Steps**

1. Generate Prediction Results: Save the prediction results from the model or algorithm into a JSONL file. Each line should be formatted as follows:
```json
{"tag": "Ground Truth Label", "judgement": "Model Judgement"}
```

2. Run Evaluation Script: Use the [binary_eval.py](./binary_eval.py) or [multi_cls_eval.py](./multi_cls_eval.py)  script to evaluate the prediction results. The script will calculate and output evaluation metrics.

Example Command:

```shell
python binary_eval.py/multi_cls_eval.py --input predictions.jsonl
```

Ensure that the predictions.jsonl file is correctly formatted and consistent with the sample format in the dataset.

