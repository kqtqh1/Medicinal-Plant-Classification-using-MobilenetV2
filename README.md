# Medicinal-Plant-Classification-using-MobilenetV2
 
## Overview
This Medicinal Plant Classification App is developed as part of a research project. It uses the MobileNetV2 model to identify different types of medicinal plants. The model was trained on 30,000 images across 35 plant classes, plus 1 class for unknown plants. The app was built using Android Studio and works offline, offering a smooth and easy-to-use experience on mobile devices.

## Table of Contents
  - [Overview](#overview)
  - [Dataset](#dataset)
  - [Preprocessing Techniques](#preprocessing-techniques)
  - [Performance Evaluation](#performance-evaluation)
  - [Adding TF Lite in Android Studio](#adding-tensorflow-lite-model-in-android-studio)
  - [App](#app)
  - [Credits](#credits)

## Dataset
The model was trained and tested using a mix of publicly available and custom-collected datasets to ensure strong performance and good variety. The dataset includes:   - Training Set: 21,600 images
 - Validation Set: 3,960 images
 - Test Set: 1,980 images
   
#### Dataset Used
* [Indian Medicinal ⚕️Leaves 🌿 Dataset](https://www.kaggle.com/datasets/aryashah2k/indian-medicinal-leaves-dataset)
* [Mango](https://universe.roboflow.com/space-5djsz/mango-t8cpv-utr95)
* [Herb Lens](https://universe.roboflow.com/mpcs/herb-lens)
* [Herbal Plants](https://universe.roboflow.com/forda-thesis-ang-ferson/herbal-plants-l0bmw)
* [Plant Detection](https://universe.roboflow.com/testerspace/plant-detection-qxcwe)
* [begonvil](https://universe.roboflow.com/space-5djsz/begonvil-7tes8)
* [flowers_segmentation](https://universe.roboflow.com/flowersdetection/flowers_segmentation)
* [pt2.calamansi.v2](https://universe.roboflow.com/new-workspace-eozul/pt2.calamansi.v2)
* [Basella Alba (Basale)](https://universe.roboflow.com/project-z499k/basella-alba-basale-mht8b)
* Custom Dataset - We also added some plant images to make the model more accurate and cover more types.

## Preprocessing Techniques
* Image Resizing
* Data Augmentation (Random rotation and brightness)
* Normalization

## Performance Evaluation
The model was trained for more than 15 epochs and tested on a dataset of 1,980 images. The evaluation results are as follows:

* Results on the Training Dataset

![Image](https://github.com/user-attachments/assets/31522fbc-2bc4-4189-9cf5-09b6916aaca6)

* Results on the Test Dataset
  - Accuracy: 86%
  - Macro Avg: 86%
  - Weighted Avg: 86%

![Image](https://github.com/user-attachments/assets/e2870297-ead8-4e44-86e1-bc5ba01369a2)


## Adding Tensorflow Lite model in Android Studio
1. Go to app/src/main and look for the asset folder. If it does not exist, create it.
2. Copy the **model.tflite** into the assets folder.
3. Open **build.gradle.kts(Module:app)** and add **'this.implementation ("org.tensorflow:tensorflow-lite:2.11.0")'** and **'this.implementation ("org.tensorflow:tensorflow-lite-select-tf-ops:2.11.0")'** to the dependencies.
    
## App

![Image](https://github.com/user-attachments/assets/673e4dbb-47d3-443e-9427-7a3b5905fd0c)

## Credits

I would like to thank the following individuals for their valuable contributions and collaboration throughout the project.

- **JanJoe Rosario** - _Researcher_ 
- **Angela Soriano** - _Researcher_ 
- **Aliyah Velazquez** - _Researcher_


