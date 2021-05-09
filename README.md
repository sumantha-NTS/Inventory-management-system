# Inventory-management-system
Efficient Inventory Management System
Inventory management is a systematic approach to sourcing, storing, and selling inventory - both raw materials (components) and finished goods (products). In business terms, inventory management means the right stock, at the right levels, in the right place, at the right time, and at the right cost as well as price.
Poor inventory management can cost you time, money and your business. It is among the top reasons why small businesses fail.

### Causes for Poor inventory management :
1. Poor Forecasting
2. Excessive stock pile-up
3. Supply chain complexity
4. Inefficient order management
5. Managing warehouse space

### Effects of Poor inventory Management :
1. Increased Costs
2. Unsatisfied Customer
3. Delayed delivery of orders
4. Imbalanced inventory 

In order to avoid the poor inventory and to upscale the business, the machine learning comes into picture where the analysis is carried out based on the past sales information and with the help of algorithms to predict the future inventory.

### Main advantages of efficient inventory management are:
1. Avoidance of stock-outs and excess stocks
2. Improved business negotiations
3. Ability to make more profitable business decisions
4. Reduced risk of overselling

This project will explain how to manage the inventory efficiently with the help of a sample dataset.

## Business Objective :

Poor inventory management leads to a loss in sales which in turn paints an inaccurate picture of lower demand for certain items, making future order predictions based on that past data inherently inaccurate.
Instead smart retailers use real-time data to move inventory where it's needed before it's too late.
The objective of this project is to make inventory management efficient using predictive analysis.

## Dataset details :
Two datasets has been considered for this project and they are
Product details
Product Revenue details

#### Product details dataset:
Product dataset consists of 1115 product type with cost per unit and time for delivery. The sample data of this dataset is given below
Sample data for product dataset 

#### Product Revenue dataset:
Revenue dataset consists of 10,17,209 records with daily data of 1115 products. The dataset consists of other columns like revenue, store status, promotion applied, Generic holiday etc. The total records in revenue dataset will constitutes for 3 years 10months data.\

Features are explained below:
1. Store Status : It's a categorical feature which explains "Is the store open or closed..?". It has two unique values i.e., open and close.
2. Promotion Applied : It's a continuous feature which explains "Is the promotion applied for the particular product or not..?". 
3. Generic Holiday : It's a continuous feature which explains "Is the particular day is a general holiday or not..?".
4. Educational Holiday : It's a continuous feature which explains "Is the particular day is a educational holiday or not..?".

## Feature Engineering:
In order to build the predictive model, two datasets are merged with respect to product type and 'No of sales' new feature has created which represent the units sold.

i.e., No. of sales = Revenue / cost per unit

After merging two datasetIn general, the inventory of the shop will be refreshed every week or month or sometimes it will be quarterly. In order to analyze the data in terms of weekly, monthly and quarterly basis, the entire dataset is converted into weekly, monthly and quarterly aggregated values respectively.

## Feature Selection:
From exploratory data analysis, it is observed that the educational holiday variable does not affect the revenue. Therefore, the educational holiday variable is neglected while building the model. The other variables are considered for the model building which is explained in next section.

## Model Building:
To build the model, the entire dataset is separated into input and output variables.

In order to remove scaling effect from input variable, MinMax scalar is used which will convert every data point between 0 and 1 since there are many categorical variable.

The no. of units variable is considered to be output variable and Log transformation is applied to bring the variable towards the normal distribution.

After transformation the entire dataset is splitted into train and test data with 80% data as train and 20% data as test.

With the above transformed data different models have been built for weekly, monthly and quarterly datasets. 

Root Mean Squared Error and R2 score is considered as evaluation metric to select the best model. All the models which are developed are optimized with hyper parameter tuning using GridSearchCV and evaluation metrics are calculated.
Below table shows the RMSE and R2 score for different model used

Evaluation metric results for weekly dataset XG Boost algorithm is considered as final model for weekly dataset.

Evaluation metric results for monthly datasetXG Boost algorithm is considered as final model for monthly dataset.

XG Boost algorithm is considered as final model for quarterly dataset.

## Model Deployment:
Finalized model shown in previous section is considered for app deployment.
The predicted stocks are added with 10% of buffer to compensate for growth in the industry and the population.\
The Web API has been developed with the help of Flask framework and deployed in Heroku platform.\

### Link of Web API : 
https://efficient-inventory.herokuapp.com/

## Conclusion:
Inventory management is a very tedious process if not done properly may lead to loss in sales, customer dissatisfaction etc. Smart retailers will use predictive analysis which will lead better management of stocks, centralized control which intern increase the productivity.
