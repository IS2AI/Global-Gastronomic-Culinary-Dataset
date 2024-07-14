# Global Food Scenes Dataset

In this work, we propose the Global Food Scenes Dataset, a followup of our previous work Central Asian Food Scenes Dataset (CAFSD) combined with Nutrition5k dataset annotated with bounding boxes. The Global Food Scenes Dataset contains 241 food classes whereas the annotated Nutrition5k dataset contains 113 classes. The statistics of classes grouped into 18 coarse classes are shown in Figure below.
![alt text](https://github.com/[IS2AI]/[Global_Food_Scenes_Dataset]/blob/[figures]/categories_subplots.png?raw=true)

# Pre-trained models
All dataset files and different models pre-trained on different datasets are available for download.

## Validation Set Results

| Model Size   | CAFSD (mAP50)  | Nutrition5k (mAP50)| GFSD (mAP50)|
|--------------|--------|-------------|---------------------|
| YOLOv8n      | 0.583  | 0.797       | 0.638               |
| YOLOv8s      | 0.642  | 0.827       | 0.690               |
| YOLOv8m      | 0.678  | 0.838       | 0.717               |
| YOLOv8l      | 0.691  | 0.824       | 0.728               |
| YOLOv8xl     | **0.699**  | **0.839**  | **0.731**               |
| RT-DETR-x    | 0.681  | 0.802  | 0.719               |

