# happymonk
Assignment A for Happymonk AI
1. Consider a large dataset (say, a time series) A. Also, consider a smaller dataset B. How do you
ensure whether sets A and B identify the same variable? Illustrate it with a Python script.

2. Collect data (images) and annotate them for two classes: Person and vehicle. You may use
platforms such as LabelImg for annotations. You may limit to 800 images for the dataset. Perform
object detection on your collected dataset and find the mean distance between the two classes
in each image. You may use YOLOv5 for detection.

Step by step Answer:
Workflow
1. Need to clone the Git yolov5 repository and necessary requirement pacakge
2. Used google collab for GPU runtime
3. As per the question need to label two class Person and vehicle so for that used
   used coco image and created a folder train_data inside images and inside that created train and val folders 
   and used MAKESENSE AI for the image labelling for the both train and val images. And I used less images for train and validation but used 
   yolov5x. for the processing it is pretrained model so  for that it has more number images and it will use that and run as per my understading
4. And i edited coco yaml file to use only for class and changed the path for train and test and renamed and updated as custom_data.yaml file for easy identification
5. !python train.py --img 640 --batch 16 --epochs 20 --data custom_data.yaml --weights yolov5x.pt --nosave --cache
    use the above comments and tested and stored the output automatically  because faced so many errors and got output so run folder of yolov5 will stored in exp5
 6.Printed the result -- thanks you

3. Download an image dataset of your choice for binary class classification. Perform the data
augmentation techniques like flipping, rotation and transformation. Apply at least two object
classification techniques both on the augmented as well as on the original dataset. Display the
performance of the Algorithms. Prepare a comparison chart.
4. Collect images of vehicles with license plates written in Indian regional languages (eg. Hindi,
Kannada, Tamil, Telugu, Bengali, etc.). Apply Image augmentation techniques on the collected
images. Maintain separate folders for different language license plates. You may limit to 800
images in the dataset including the augmented images.
