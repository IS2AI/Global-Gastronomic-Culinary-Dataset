# Global Food Scenes Dataset

In this work, we propose the Global Food Scenes Dataset, a followup of our previous work Central Asian Food Scenes Dataset (CAFSD) combined with Nutrition5k dataset annotated with bounding boxes. The Global Food Scenes Dataset contains 241 food classes whereas the annotated Nutrition5k dataset contains 113 classes. The statistics of classes grouped into 18 coarse classes are shown in Figure below.
![alt text](https://github.com/[IS2AI]/[Global_Food_Scenes_Dataset]/blob/[figures]/categories_subplots.png?raw=true)

# Pre-trained models
All dataset files and different models pre-trained on different datasets are available for download.

## Validation Set Results

| Model Size      | CAFSD  |           | Google |           | CAFSD+Google v3+aug |           |
|-----------------|--------|-----------|--------|-----------|----------------------|-----------|
|                 | mAP50  | mAP95     | mAP50  | mAP95     | mAP50                | mAP95     |
| YOLOv8n         | 0.583  | 0.501     | 0.797  | 0.707     | 0.638                | 0.554     |
| YOLOv8s         | 0.642  | 0.562     | 0.827  | 0.738     | 0.690                | 0.608     |
| YOLOv8m         | 0.678  | 0.605     | 0.838  | 0.758     | 0.717                | 0.642     |
| YOLOv8l         | 0.691  | 0.619     | 0.824  | 0.744     | 0.728                | 0.656     |
| YOLOv8xl        | **0.699**  | **0.625**     | **0.839**  | **0.759**     | **0.731**                | **0.661**     |
| RT-DETR-l       | 0.639  | 0.569     | 0.805  | 0.719     | 0.676                | 0.599     |
| DETR            | 0.507  | 0.394     | 0.685  | 0.523     | 0.541                | 0.423     |
| RT-DETR-x freeze=6 | 0.681  | 0.611     | 0.802  | 0.725     | 0.719                | 0.646     |
