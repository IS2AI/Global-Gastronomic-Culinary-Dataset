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

