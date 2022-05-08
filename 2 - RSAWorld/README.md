
# AutoGrader (Paper2Excel)
This won't help you convert .doc, .pdf, .ppt to excel. It will help you convert the actual paper to excel! Be it a table or a bubble sheet just take a picture of it and watch it magically become the original excel file!

>This serves as the project for the image processing course taught to juniors in CUFE for 2022.
## Technologies
<br>
<div align='center'>
<img src="/Demo/python.png" width="10%"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/Demo/pytorch.png" title="Your Github should be on dark mode." width="30%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/Demo/image.png" width="10%"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/Demo/flask.png" width="30%">
</div>
<br>
<div align='center'>
<img src="/Demo/Tesseract.png" title="Tesseract OCR was only used to gauge our performance" width="30%">
</div>


## Running the Application

1. Clone the repository
```
$ git clone https://github.com/radwaahmed2132000/Auto-Grader
```

2. Start the Virtual Environment
```
$ pipenv install && pipenv shell
```

3. Install the requirements
```
$ pip install -r requirements.txt
```

4. Run the Flask App
```
$ python app.py
```
## Quick Demo
### Ready?
![image](https://user-images.githubusercontent.com/49572294/148289714-b572b7a7-60e9-431c-b3d0-7242ae83a27c.png)
### Let's go!
<img src="/Demo/Video.gif" >

### Classification Accuracy
![image](https://user-images.githubusercontent.com/49572294/152766243-71ce0e17-c4f9-4774-b51d-a9676cad84b9.png)
<img src="/Demo/Handwritten.png" width="41%" title="vertical lines should return their count, horizontal lines should return 5 - count" >

### Serious Challenge?
<div align="center">
<img src="/Demo/Survive.png" width="100%" title="vertical lines should return their count, horizontal lines should return 5 - count" >
</div>

### For each cell we scan and before further processing, we feed the result int Google's Tesseract OCR (which isn't designed for this type of task) and to our classifier.

### OCR Results
<img src="/Demo/Google.png" width="100%" title="vertical lines should return their count, horizontal lines should return 5 - count" >

### Our Results (HexClassifier & PrintClassifier)
<img src="/Demo/Real.png" width="100%" title="vertical lines should return their count, horizontal lines should return 5 - count" >

### Wait! This is just half of the project, there's also 

<img src="/Demo/Bubble.png" width="100%" title="vertical lines should return their count, horizontal lines should return 5 - count" >

### You give us this and an answers text file

<img src="/Demo/BubbleSheet.jpeg" width="50%" title="vertical lines should return their count, horizontal lines should return 5 - count" >

### And we return how the student did! Check the Bubble Sheet branch for more.

## Machine Learning Notes

ANNs were the only deep learning method allowed, two classifiers were designed. One that classifies handwritten hexadecimal digits (HexClassifier) and another that classifies printed digits (PrintClassifier). The EMNIST dataset was used for the former (after excluding the unneeded letters) and <a href="https://www.kaggle.com/dhruvmomoman/printed-digits"> this dataset </a> for printed digits (after some preprocessing.)

## System Design & More

Check the proposal document attached.


