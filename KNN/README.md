# KNN TO CANCER DATASET

This dataset has a total of 30 features related to cancers tumors (tumor radius, perimeters and others) and a single target (tumor benign/malignant). 
<br />The objective is to use **KNN algorithm** to classifying whether a person's tumor will be malignant or benign, based on features provided. 
<br />I will avoid further explanations of this algorithm, due to the large amount of documentation available. 

## DATA ANALISYS
Data table:
<p align="center">
<img src="./imgs/01.PNG" width=90% height=40% align="center">
  <br />We have 30 features and a single target (0/1).
</p>


Below, is the heatmap. Due to the large amount of features, the visualization is not so fast.
<p align="center">
<img src="./imgs/02.PNG" width=90% height=40% align="center">
  <br />Heatmap.
</p>

As KNN needs a K value to process the algorithm, I will run tests with different K values to find the best score.
<p align="center">
<img src="./imgs/03.PNG" width=90% height=40% align="center">
  <br />The optimal K is 13.
</p>


<br /><br />
## MODEL EVALUATION AND IMPROVEMENTS

In the model has predicted 9 Benign Tumors but they are Malign Tumors (False Negative). This type of error is worrying since it is a cancer prediction.
<p float="left" align="center">
<img src="./imgs/04.PNG" width=40% height=50%>
<br />Confusion Matrix. 
</p>


<br /><br />About the classification report, the accuracy seems good (0.96). Related to False Negative erros, the precision and recall to benign turmos got too low (0.93 for both).
<p float="left" align="center">
<img src="./imgs/05.PNG" width=40% height=50%>
<br />Classification Report
</p>


<br /><br />As improvement, we could get a better heatmap by grouping some columns that are similar (maybe PCA method). 
<br />A second point, it would be interesting create a algorithm to determine which parameter is most likely to imply a malignant tumor.
<br />Another improvement point is to try KNN variations to reduce the Recall/False Negative problem.
