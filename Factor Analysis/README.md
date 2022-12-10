# FACTOR ANALYSIS 

## **UNDER CONSTRUCTION**

The objective here is apply **Factor Analysis**, explore it and learn profile of factors.

## THE DATA SET
This specific dataset shows a online marketplace of cars in USA. There are informations about the cars, price and location. All features names are easy to interpret.

## DATA PRE PROCESSING
First, the data info:

<p align="center">
<img src="./imgs/01.PNG" width=60% height=50% align="center">
</p>
Data Info and Count of Income / Education Level.
<br /><br />
As we can see, most part of the features are categorical and 3 continous. 

## SOME ANALYSE

<p align="center">
<img src="./imgs/02.PNG" width=55% height=50% align="center">
  <br />Correlation Heatmap.
</p>
<br /><br />



<p align="center">
<img src="./imgs/03.PNG" width=70% height=40% align="center">
  <br />P-value for all correlations.
</p>
<br /><br />

## STARTING FACTOR ANALYSIS

<br /><br />
<p align="center">
<img src="./imgs/08.PNG" width=75% height=55% align="center">
  <br />Sphericity Bartlett Test.
</p>
<br /><br />


<br /><br />
<p align="center">
<img src="./imgs/04.PNG" width=75% height=55% align="center">
  <br />Eigen Values.
</p>
<br /><br />

<br /><br />
<p align="center">
<img src="./imgs/05.PNG" width=85% height=60% align="center">
  <br />Kaiser Criteria.
</p>
<br /><br />

## FACTORS

**From distribution of clusters:**
<br /><br /><br />
<p align="center">
<img src="./imgs/07.PNG" width=85% height=60% align="center">
  <br />Factors.
</p>
<br /><br />

**Insights**
<br />
-**Factor 00**: This factor indicates strongly and inversely associated to fuel and average  type and price of cars 
-**Factors 01, 02 and 03**: These factors are highly related, directly proporcional to price, cylinders of cars and drive, respectively.
-**Factor 04**: Related to year and transmission of cars.
-**Factor 05, 06 and 07**: Softly association. Factors 05 and 07 have directly correlation, whereas factor 06 is inversely correlation. Factor 05 means the state located, factor 06 condition of transmition. And last one, car's condition.

<br />