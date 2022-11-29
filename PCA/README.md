# CLUSTERING IN A BANK CHURN DATA


The objective here is apply **Agglomerative Clustering**, explore it and learn profile of clusters, apply **Principal Component Cnalysis (PCA)** to get reduce all features and check how it behaves. 

## THE DATA SET
This specific dataset shows a bank's churn in last 12 months. Churn is the information which customers stop doing business with a company over a given period of time. Although the columns are named and easily interpreted, some may raise questions:

**-Attrition_Flag** - Attrition Flag means account closed and Existing means not closed.
<br />**-Total_Relationship_Count** - Total no. of products held by the customer
<br />**-Months_Inactive_12_mon** - No. of months inactive in the last 12 months
<br />**-Contacts_Count_12_mon** - No. of Contacts in the last 12 months
<br />**-Total_Revolving_Bal** - Total Revolving Balance on the Credit Card
<br />**-Avg_Open_To_Buy** - Open to Buy Credit Line (Average of last 12 months)
<br />**-Total_Amt_Chng_Q4_Q1** - Change in Transaction Amount (Q4 over Q1)
<br />**-Total_Trans_Amt** - Total Transaction Amount (Last 12 months)
<br />**-Total_Trans_Ct** - Total Transaction Count (Last 12 months)
<br />**-Total_Ct_Chng_Q4_Q1** - Change in Transaction Count (Q4 over Q1)
<br />**-Avg_Utilization_Ratio** - Average Card Utilization Ratio


## DATA PRE PROCESSING
First, the data info:

<p align="center">
<img src="./imgs/01.PNG" width=60% height=50% align="center">
</p>
Data Info and Count of Income / Education Level.
<br /><br />
We have some 'object' columns that must be handled and some 'unknown' data. I'll remove unknown. Moreover, there are some outliers data that will be removed. After filter data, the features will be transformed to numeric and apply zscore (Standard Scaler).


## CLUSTERING
To know the best number of clusters, Elbow method:
<p align="center">
<img src="./imgs/04.PNG" width=55% height=50% align="center">
  <br />Elbow Method.
</p>
<br /><br />

After apply **Agglomerative Clustering** with k=7, we can apply **PCA** with k=3 and take a look how clusters are divided.

<p align="center">
<img src="./imgs/05.PNG" width=70% height=40% align="center">
  <br />Clusters with PCA.
</p>
<br /><br />

## ANALYSIS

<br /><br />
<p align="center">
<img src="./imgs/03.PNG" width=75% height=55% align="center">
  <br />Heatmap with correlation between features.
</p>
<br /><br />


<br /><br />
<p align="center">
<img src="./imgs/06.PNG" width=75% height=55% align="center">
  <br />Distribution of Clusters.
</p>
<br /><br />

<br /><br />
<p align="center">
<img src="./imgs/07.PNG" width=85% height=60% align="center">
  <br />Some Clusters' features.
</p>
<br /><br />

## NOTES

**From distribution of clusters:**
<br />I won't analyse every cluster, but the attention goes to **cluster 05.**
*It has **100% attrited customers.**
*Even making a lot of transactions/month, this cluster has low utilization ratio (only blue card).
*They have low income, low credit limit and low open to buy.

**From heatmap:**
<br />The lower of products held by the customer, the greater is the transaction amount (-0,35). 
Is possible to check that the amount of products held by the customer is not related to average utilization ratio (0,073).

<br />