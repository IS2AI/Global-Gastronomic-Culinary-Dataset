# Global Food Scenes Dataset

In this work, we propose the Global Food Scenes Dataset, a followup of our previous work Central Asian Food Scenes Dataset (CAFSD) combined with Nutrition5k dataset[1] annotated with bounding boxes. We annotated the Nutrition5k dataset with bounding boxes resulting in 12,839 images across 113 classes. The final combined dataset which we call Global Food Scenes Dataset contains 34,145 images across 241 food classes. Some visual examples of a few classes are shown for the annotated Nutrition5k and CAFSD datasets in the figure below. 
![Alt text](figures/paper_front.png)

The statistics of classes grouped into 18 coarse categories are shown in Figure below.
![Alt text](figures/categories_subplots.png)

In this Github repo, you can find everything used in this project including training scripts, data preparation scripts, datasets, pre-trained models, and so on.


# Download Datasets and Pre-trained models
All dataset files and different models pre-trained on different datasets are available for download.   
To download the Global Food Scenes Dataset (GFSD): https://issai.nu.edu.kz/wp-content/themes/issai-new/data/models/GFSD/GFSD.zip  
To download the annotated Nutrition5k dataset: https://issai.nu.edu.kz/wp-content/themes/issai-new/data/models/Nutrition5k/Nutrition5k.zip  
YOLOv8n model trained on the annotated Nutrition5k dataset: https://issai.nu.edu.kz/wp-content/themes/issai-new/data/models/Nutrition5k/yolov8n.pt  
YOLOv8s model trained on the Global Food Scenes Dataset (GFSD): https://issai.nu.edu.kz/wp-content/themes/issai-new/data/models/GFSD/yolov8s.pt  
RT-DETR-x model trained on the Central Asian Food Scenes Dataset (CAFSD): https://issai.nu.edu.kz/wp-content/themes/issai-new/data/models/CAFSD/rtdetr-x.pt  

## Validation Set Results

| Model Size   | CAFSD (mAP50)  | Nutrition5k (mAP50)| GFSD (mAP50)|
|--------------|--------|-------------|---------------------|
| YOLOv8n      | 0.583  | 0.797       | 0.638               |
| YOLOv8s      | 0.642  | 0.827       | 0.690               |
| YOLOv8m      | 0.678  | 0.838       | 0.717               |
| YOLOv8l      | 0.691  | 0.824       | 0.728               |
| YOLOv8xl     | **0.699**  | **0.839**  | **0.731**               |
| RT-DETR-x    | 0.681  | 0.802  | 0.719               |


## References
[1] Thames, Q., Karpur, A., Norris, W., Xia, F., Panait, L., Weyand, T., & Sim, J. (2021). Nutrition5k: Towards automatic nutritional understanding of generic food. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 8903–8911).
