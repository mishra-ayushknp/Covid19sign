
## Project Motivation

The Project can be used for following purposes:

1. **Training a CNN model on the given Image Dataset**
     Use [covid19p.py](Classes/dataset_preparation.py) to resize all the images into 150x150 Pixels, then converting the PNG format dataset and their labels(covid19 or normal) into Pickle as the Model will take them in form of pickle dataset.
- The above program will generate two pickle files(xe.pickle, ye.pickle) in same [Classes](Classes/ct_scans_png_dataset.rar) directory, we have also provided generated pickle files for same [dataset], so that you can use these pickle files directly in generating CNN Model by using [model.py].
- The program([model.py](Classes/model.py)) will generate a saved model file .
2. **Convert all the image in same format(using .png)**
     Use [renameimage.py] to convert into png format .
3. **Predicting CT Scan Image**
    After training the model on the dataset, use [prediction.py](Classes/predict_ct_scan.py) to test on any lung ct scan image, the program will first resize the image to 150 x 150 pixel size, then loads the image into model and print the type of scan(Covid-19 or Normal Scan). It should be noted that the prediction of model is based on these parameters: Training Accuracy, Training Loss, Validation Accuracy and Validation Loss for the given dataset and the trained model architecture.

Detects Covid-19 Pneumonia signs from CT Scan Images by a CNN Model. The model have a uniform dataset of 764 Images of CT Scan which consist 349 Images of Covid-19 Pneumonia affected patients and remaining shows normal patient scans.
