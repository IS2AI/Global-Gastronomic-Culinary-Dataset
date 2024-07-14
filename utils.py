
import os
import shutil
import pandas as pd
from tqdm import tqdm
import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
from pathlib import Path
import json
from PIL import Image




###############################################################################################################################################################
# CODE FOR MAPPING YOLO CLASS LABELS
 
def create_mapping(classes):
    mapping = {}
    for idx, cls in enumerate(sorted(classes)):
        mapping[cls] = idx
    return mapping

def get_name_by_index(index, my_dict):
    for name, idx in my_dict.items():
        if idx == int(index):
            return name
    return None

def update_labels(label_file, old_mapping, new_mapping):
    with open(label_file, 'r') as f:
        lines = f.readlines()
    print(f'Updating labels in {label_file} ....')
    print('Old labels: ', lines)
    updated_lines = []
    for line in lines:
        if len(line.split()) == 5:
            class_id = line.split()[0]
            class_name = get_name_by_index(class_id, old_mapping)
            if class_name in new_mapping:
                updated_class_id = new_mapping[class_name]   
                updated_line = f"{updated_class_id} {' '.join(line.split()[1:])}"
                updated_lines.append(updated_line)
                print(f'Mapped the class {class_name} from old id of {class_id} to {updated_class_id}')
            else:
                print(f'Deleting the label for class {class_name} as it is not found in new mapping')
    with open(label_file, 'w') as f:
        for item in updated_lines:
            f.write(item + '\n')
    print('Updated labels: ', updated_lines)
    print('\n\n')

folder1 = ['airan-katyk', 'almond', 'apple', 'artichoke', 'arugula', 'asparagus', 'avocado', 'bacon', 'banana', 'beans', 'beet', 'bell pepper', 'black olives', 'blackberry', 'blueberry', 'boiled chicken', 'bread', 'broccoli', 'buckwheat', 'cabbage', 'cakes', 'carrot', 'cashew', 'casserole with meat and vegetables', 'cauliflower', 'celery', 'cereal based cooked food', 'cheese', 'chickpeas', 'chips', 'cooked eggplant', 'cooked food based on meat', 'cooked food meat with vegetables', 'cooked zucchini', 'cookies', 'corn', 'crepe', 'cucumber', 'cutlet', 'desserts', 'egg product', 'fish', 'fried chicken', 'fried eggs', 'fried fish', 'fried meat', 'fruits', 'granola', 'grapes', 'green beans', 'herbs', 'hummus', 'ice-cream', 'juice', 'kiwi', 'lavash', 'legumes', 'lemon', 'mandarin', 'mashed potato', 'meat product', 'melon', 'mixed berries', 'mixed nuts', 'mushrooms', 'onion', 'orange', 'pasta', 'pastry', 'peanut', 'pear', 'peas', 'pecan', 'pickled cabbage', 'pickled squash', 'pie', 'pineapple', 'pizza', 'plov', 'porridge', 'potatoes', 'pumpkin', 'radish', 'raspberry', 'rice', 'salad fresh', 'salad leaves', 'salad with fried meat veggie', 'salad with sauce', 'sandwich', 'sausages', 'seafood', 'snacks bread', 'souces', 'soup-plain', 'soy product', 'spinach', 'strawberry', 'suzbe', 'sweet potatoes', 'tomato', 'tomato souce', 'tushpara-wo-soup', 'vegetable based cooked food', 'waffles', 'walnut', 'watermelon', 'zucchini']
folder2 = ['airan-katyk', 'almond', 'apple', 'arugula', 'asparagus', 'avocado', 'bacon', 'banana', 'beans', 'beet', 'bell pepper', 'black olives', 'blackberry', 'blueberry', 'boiled chicken', 'bread', 'broccoli', 'cabbage', 'carrot', 'cashew', 'casserole with meat and vegetables', 'cauliflower', 'celery', 'cereal based cooked food', 'cheese', 'chickpeas', 'chips', 'cooked eggplant', 'cooked food based on meat', 'cooked food meat with vegetables', 'cooked zucchini', 'cookies', 'corn', 'cucumber', 'cutlet', 'desserts', 'egg product', 'eggplant', 'fish', 'fried chicken', 'fried fish', 'fried meat', 'fruits', 'granola', 'grapes', 'green beans', 'herbs', 'hummus', 'ice-cream', 'irimshik', 'juice', 'kiwi', 'lavash', 'lemon', 'mandarin', 'mango', 'meat product', 'melon', 'mixed berries', 'mixed nuts', 'mushrooms', 'onion', 'orange', 'pasta', 'pastry', 'pear', 'peas', 'pecan', 'pickled cabbage', 'pickled squash', 'pie', 'pineapple', 'pizza', 'porridge', 'potatoes', 'radish', 'raspberry', 'rice', 'salad fresh', 'salad with fried meat veggie', 'salad with sauce', 'sausages', 'seafood', 'smetana', 'snacks', 'snacks bread', 'souces', 'soup-plain', 'soy product', 'spinach', 'strawberry', 'suzbe', 'sweet potatoes', 'tomato', 'tushpara-wo-soup', 'vegetable based cooked food', 'waffles', 'walnut', 'watermelon']
cafsd = ['achichuk', 'airan-katyk', 'almond', 'apple', 'apricot', 'artichoke', 'arugula', 'asip', 'asparagus', 'avocado', 'bacon', 'baklava', 'banana', 'basil', 'bauyrsak', 'bean soup', 'beans', 'beef shashlyk', 'beef shashlyk-v', 'beer', 'beet', 'bell pepper', 'beshbarmak', 'beverages', 'black olives', 'blackberry', 'blueberry', 'boiled chicken', 'boiled eggs', 'boiled meat', 'borsch', 'bread', 'brizol', 'broccoli', 'buckwheat', 'butter', 'cabbage', 'cakes', 'carrot', 'cashew', 'casserole with meat and vegetables', 'cauliflower', 'caviar', 'celery', 'cereal based cooked food', 'chak-chak', 'cheburek', 'cheese', 'cheese souce', 'cherry', 'chestnuts', 'chicken shashlyk', 'chicken shashlyk-v', 'chickpeas', 'chili pepper', 'chips', 'chocolate', 'chocolate paste', 'cinnabons', 'coffee', 'condensed milk', 'cooked eggplant', 'cooked food based on meat', 'cooked food meat with vegetables', 'cooked tomatoes', 'cooked zucchini', 'cookies', 'corn', 'corn flakes', 'crepe', 'crepe w filling', 'croissant', 'croissant sandwich', 'cucumber', 'cutlet', 'dates', 'desserts', 'dill', 'doner-lavash', 'doner-nan', 'dragon fruit', 'dried fruits', 'egg product', 'eggplant', 'figs', 'fish', 'french fries', 'fried cheese', 'fried chicken', 'fried eggs', 'fried fish', 'fried meat', 'fruits', 'garlic', 'granola', 'grapefruit', 'grapes', 'green beans', 'green olives', 'hachapuri', 'hamburger', 'hazelnut', 'herbs', 'hinkali', 'honey', 'hot dog', 'hummus', 'hvorost', 'ice-cream', 'irimshik', 'jam', 'juice', 'karta', 'kattama-nan', 'kazy-karta', 'ketchup', 'kiwi', 'kurt', 'kuyrdak', 'kymyz-kymyran', 'lagman-fried', 'lagman-w-soup', 'lavash', 'legumes', 'lemon', 'lime', 'mandarin', 'mango', 'manty', 'mashed potato', 'mayonnaise', 'meat based soup', 'meat product', 'melon', 'milk', 'minced meat shashlyk', 'mint', 'mixed berries', 'mixed nuts', 'muffin', 'mushrooms', 'naryn', 'nauryz-kozhe', 'noodles soup', 'nuggets', 'oil', 'okra', 'okroshka', 'olivie', 'onion', 'onion rings', 'orama', 'orange', 'pancakes', 'parsley', 'pasta', 'pastry', 'peach', 'peanut', 'pear', 'peas', 'pecan', 'persimmon', 'pickled cabbage', 'pickled cucumber', 'pickled ginger', 'pickled squash', 'pie', 'pineapple', 'pistachio', 'pizza', 'plov', 'plum', 'pomegranate', 'porridge', 'potatoes', 'pumpkin', 'pumpkin seeds', 'quince', 'radish', 'raspberry', 'redcurrant', 'ribs', 'rice', 'rosemary', 'salad fresh', 'salad leaves', 'salad with fried meat veggie', 'salad with sauce', 'samsa', 'sandwich', 'sausages', 'scallion', 'seafood', 'seafood soup', 'sheep-head', 'shelpek', 'shorpa', 'shorpa chicken', 'smetana', 'smoked fish', 'snacks', 'snacks bread', 'soda', 'souces', 'soup-plain', 'soy souce', 'spinach', 'spirits', 'strawberry', 'sugar', 'sushi', 'sushi fish', 'sushi nori', 'sushki', 'suzbe', 'sweets', 'syrniki', 'taba-nan', 'talkan-zhent', 'tartar', 'tea', 'tomato', 'tomato souce', 'tomato-cucumber-salad', 'tushpara-fried', 'tushpara-w-soup', 'tushpara-wo-soup', 'vareniki', 'vegetable based cooked food', 'vegetable soup', 'waffles', 'walnut', 'wasabi', 'water', 'watermelon', 'wine', 'wings', 'zucchini']


google_classes = set(folder1 + folder2)
all_classes = set(folder1 + folder2 + cafsd)

assert len(google_classes) == 113
assert len(all_classes) == 241

#with open('./new_google_dataset_classes.txt', 'w') as f:
#    for cls in sorted(google_classes):
#       f.write(cls + '\n')

old_mapping = create_mapping(all_classes)
new_mapping = create_mapping(google_classes)



labelfolder = '../datasets/Nutrition5k/train/labels'
for labelfile in tqdm(sorted(os.listdir(labelfolder))):
    labelfilepath = os.path.join(labelfolder, labelfile)
    update_labels(labelfilepath, old_mapping, new_mapping)

  







###############################################################################################################################################################
# CODE FOR SPLITTING THE DATASET INTO TRAIN/TEST/VAL
 
def split_data(source_images_folder, source_labels_folder, destination_folder, train_ratio=0.8):
    # read files
    image_files = os.listdir(source_images_folder)
    # split into training, testing, validation sets
    random.seed(100)
    random.shuffle(image_files)
    split_1 = int(train_ratio * len(image_files))
    split_2 = int((train_ratio + (1-train_ratio)/2) * len(image_files))
    train_images = image_files[:split_1]
    test_images = image_files[split_1:split_2]
    val_images = image_files[split_2:]
    # write to a destination folder
    destination_folder.mkdir(parents=True, exist_ok=True)
    splits = [train_images, val_images, test_images]
    for i in range(3):
        if i == 0:
            split_folder = 'train'
        elif i == 1:
            split_folder = 'test'
        else:
            split_folder = 'val'
        for image in splits[i]:
            image_path = os.path.join(source_images_folder, image) 
            destination_image_path = destination_folder / split_folder / "images" / image
            destination_image_path.parent.mkdir(parents=True, exist_ok=True)
            label_file = image.rsplit(".", 1)[0] + '.txt'
            label_path = os.path.join(source_labels_folder, label_file)
            destination_label_path = destination_folder / split_folder / "labels" / label_file
            destination_label_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(label_path, destination_label_path)
            shutil.copy2(image_path, destination_image_path)
            print("Image copied to ", destination_image_path)
    
    print(f"Number of train images: {len(train_images)}\n", 
          f"Number of validation images: {len(val_images)}\n",
          f"Number of test images: {len(test_images)}\n",)





source_images_folder = Path('../datasets/Nutrition5k/train/images')
source_labels_folder = Path('../datasets/Nutrition5k/train/labels')
destination_folder = Path('../datasets/new')
split_data(source_images_folder, source_labels_folder, destination_folder, train_ratio=0.8)
 
         



###############################################################################################################################################################
# CODE FOR CONVERTING YOLO LABELS TO COCO FORMAT
 
def yolo_to_coco(yolo_bbox, img_width, img_height):
    x_center, y_center, width, height = yolo_bbox
    x_center *= img_width
    y_center *= img_height
    width *= img_width
    height *= img_height
    x_min = x_center - width / 2
    y_min = y_center - height / 2
    return [x_min, y_min, width, height]

def convert_to_coco_format(image_dir, label_dir, output_json, categories):
    images = []
    annotations = []
    annotation_id = 1

    for image_file in os.listdir(image_dir):
        if not image_file.endswith(('.jpg', '.png')):
            continue
        
        image_id = len(images) + 1
        img_path = os.path.join(image_dir, image_file)
        img = Image.open(img_path)
        width, height = img.size
        
        images.append({
            "id": image_id,
            "width": width,
            "height": height,
            "file_name": image_file
        })

        label_file = os.path.join(label_dir, os.path.splitext(image_file)[0] + '.txt')
        if not os.path.exists(label_file):
            continue
        
        with open(label_file) as f:
            for line in f:
                class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.strip().split())
                bbox = yolo_to_coco([x_center, y_center, bbox_width, bbox_height], width, height)
                
                annotations.append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": int(class_id) + 1,
                    "bbox": bbox,
                    "area": bbox[2] * bbox[3],
                    "iscrowd": 0,
                    "segmentation": []
                })
                annotation_id += 1

    coco_format = {
        "images": images,
        "annotations": annotations,
        "categories": categories
    }

    with open(output_json, 'w') as f:
        json.dump(coco_format, f, indent=4)



class_names = ['airan-katyk', 'almond', 'apple', 'artichoke', 'arugula', 'asparagus', 'avocado', 'bacon', 'banana', 'beans', 'beet', 'bell pepper', 'black olives', 'blackberry', 'blueberry', 'boiled chicken', 'bread', 'broccoli', 'buckwheat', 'cabbage', 'cakes', 'carrot', 'cashew', 'casserole with meat and vegetables', 'cauliflower', 'celery', 'cereal based cooked food', 'cheese', 'chickpeas', 'chips', 'cooked eggplant', 'cooked food based on meat', 'cooked food meat with vegetables', 'cooked zucchini', 'cookies', 'corn', 'crepe', 'cucumber', 'cutlet', 'desserts', 'egg product', 'eggplant', 'fish', 'fried chicken', 'fried eggs', 'fried fish', 'fried meat', 'fruits', 'granola', 'grapes', 'green beans', 'herbs', 'hummus', 'ice-cream', 'irimshik', 'juice', 'kiwi', 'lavash', 'legumes', 'lemon', 'mandarin', 'mango', 'mashed potato', 'meat product', 'melon', 'mixed berries', 'mixed nuts', 'mushrooms', 'onion', 'orange', 'pasta', 'pastry', 'peanut', 'pear', 'peas', 'pecan', 'pickled cabbage', 'pickled squash', 'pie', 'pineapple', 'pizza', 'plov', 'porridge', 'potatoes', 'pumpkin', 'radish', 'raspberry', 'rice', 'salad fresh', 'salad leaves', 'salad with fried meat veggie', 'salad with sauce', 'sandwich', 'sausages', 'seafood', 'smetana', 'snacks', 'snacks bread', 'souces', 'soup-plain', 'soy product', 'spinach', 'strawberry', 'suzbe', 'sweet potatoes', 'tomato', 'tomato souce', 'tushpara-wo-soup', 'vegetable based cooked food', 'waffles', 'walnut', 'watermelon', 'zucchini']
assert len(class_names) == 113
categories = [{"id": i + 1, "name": name, "supercategory": "none"} for i, name in enumerate(class_names)]

    
dataset_dir = '../datasets/Nutrition5k'
output_dir = '../datasets/Nutrition5k/annotations'
os.makedirs(output_dir, exist_ok=True)
    
for split in ['train', 'val', 'test']:
    image_dir = os.path.join(dataset_dir, split, 'images')
    label_dir = os.path.join(dataset_dir, split, 'labels')
    output_json = os.path.join(output_dir, f'instances_{split}.json')
    convert_to_coco_format(image_dir, label_dir, output_json, categories)



 




