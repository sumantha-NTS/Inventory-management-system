# Inventory-management-system
Efficient Inventory Management System
Inventory management is a systematic approach to sourcing, storing, and selling inventory - both raw materials (components) and finished goods (products). In business terms, inventory management means the right stock, at the right levels, in the right place, at the right time, and at the right cost as well as price.
Poor inventory management can cost you time, money and your business. It is among the top reasons why small businesses fail.
Causes for Poor inventory management :
Poor Forecasting
Excessive stock pile-up
Supply chain complexity
Inefficient order management
Managing warehouse space

Effects of Poor inventory Management :
Increased Costs
Unsatisfied Customer
Delayed delivery of orders
Imbalanced inventory

In order to avoid the poor inventory and to upscale the business, the machine learning comes into picture where the analysis is carried out based on the past sales information and with the help of algorithms to predict the future inventory.
The main advantages of efficient inventory management are:
Avoidance of stock-outs and excess stocks
Improved business negotiations
Ability to make more profitable business decisions
Reduced risk of overselling

This project will explain how to manage the inventory efficiently with the help of a sample dataset.
Business Objective :

Poor inventory management leads to a loss in sales which in turn paints an inaccurate picture of lower demand for certain items, making future order predictions based on that past data inherently inaccurate.
Instead smart retailers use real-time data to move inventory where it's needed before it's too late.
The objective of this project is to make inventory management efficient using predictive analysis.
2. Project Architecture / project flow :
Project flow of this project is defined below.
3. Dataset details :
Two datasets has been considered for this project and they are
Product details
Product Revenue details

Product details dataset:
Product dataset consists of 1115 product type with cost per unit and time for delivery. The sample data of this dataset is given below
Sample data for product datasetProduct Revenue dataset:
Revenue dataset consists of 10,17,209 records with daily data of 1115 products. The dataset consists of other columns like revenue, store status, promotion applied, Generic holiday etc. The total records in revenue dataset will constitutes for 3 years 10months data. The sample data is shown below.
Sample data for revenue datasetFeature details:
Store Status : It's a categorical feature which explains "Is the store open or closed..?". It has two unique values i.e., open and close.
Promotion Applied : It's a continuous feature which explains "Is the promotion applied for the particular product or not..?". 
Generic Holiday : It's a continuous feature which explains "Is the particular day is a general holiday or not..?".
Educational Holiday : It's a continuous feature which explains "Is the particular day is a educational holiday or not..?".
4. Exploratory Data Analysis (EDA):
Exploratory data analysis is importance step predictive analysis as it helps to get insights from the existing dataset.
Histogram is plotted to understand the distribution of the products with respect to cost per unit and time for delivery.
Boxplot is considered to understand the behavior of Promotion applied and Education holiday variable with respect to revenue.
Boxplot is considered to understand the behavior of Store status and Generic holiday variable with respect to revenue.
From the above visualizations, it is observed that there are outliers present in the data.
To check how many products have high cost per unit and low time for delivery which in term increase the business.
Products with cost per unit > 1800 and time for delivery < 6 days To check how many products have low cost per unit and high time for delivery which won't make much business.
Products with cost per unit <100 and time for delivery > 10 days5. Feature Engineering:
In order to build the predictive model, two datasets are merged with respect to product type and 'No of sales' new feature has created which represent the units sold.
i.e., No. of sales = Revenue / cost per unit
After updating the above features, the sample dataset is shown below.
After merging two datasetIn general, the inventory of the shop will be refreshed every week or month or sometimes it will be quarterly. In order to analyze the data in terms of weekly, monthly and quarterly basis, the entire dataset is converted into weekly, monthly and quarterly aggregated values respectively.
The sample data for weekly, monthly and quarterly datasets are shown below 
Sample data of weekly datasetSample data of monthly datasetSample data of quarterly datasetBar plots are used understand the most sold products in weekly, monthly basis.
Top 25 Products sold in 1st weekTop 25 Products sold in 1st month6. Feature Selection:
From exploratory data analysis, it is observed that the educational holiday variable does not affect the revenue. Therefore, the educational holiday variable is neglected while building the model. The other variables are considered for the model building which is explained in next section.
7. Model Building:
To build the model, the entire dataset is separated into input and output variables.
The sample code for the same is shown below
#consider weekly dataset
x = weekly.drop('no_of_units',axis=1)
y = weekly.no_of_units
In order to remove scaling effect from input variable, MinMax scalar is used which will convert every data point between 0 and 1 since there are many categorical variable.
The sample code for applying MinMax scalar on weekly dataset is as shown below.
#preprocessing the data i.e., applying min-max scalar
from sklearn.preprocessing import MinMaxScaler
#appling scaling for weekly data
scale_week = MinMaxScaler()
a = scale_week.fit_transform(x)
x1 = pd.DataFrame(a,columns=x.columns)
Output of above code:
Input variables of weekly data after MinMax transformationThe no. of units variable is considered to be output variable and Log transformation is applied to bring the variable towards the normal distribution.
Sample code for transforming the output variable using Log transformation is shown below.
#transforming the output variable
y1 = np.round(np.log(y))
Output of the above code:
Output variables after Log transformationAfter transformation the entire dataset is splitted into train and test data with 80% data as train and 20% data as test.
Sample code for the same is as shown as below
#Splitting weekly data into train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x1,y1,test_size=0.2,random_state=2)
print('Shape of Splitting')
print('x_train={}, y_train={}, x_test={}, y_test={}' .format(x_train.shape,y_train.shape,x_test.shape,y_test.shape))
Output of the above code:
Shape of splitting of dataWith the above transformed data different models have been built for weekly, monthly and quarterly datasets. Root Mean Squared Error and R2 score is considered as evaluation metric to select the best model.
All the models which are developed are optimized with hyper parameter tuning using GridSearchCV and evaluation metrics are calculated.
Below table shows the RMSE and R2 score for different model used
Evaluation metric results for weekly dataset XG Boost algorithm is considered as final model for weekly dataset.
Sample code for fitting the model for weekly dataset and predicting for test data is shown below
#Final Model for weekly dataset
final_weekly = XGBoostClassifier(n_estimators=500,max_depth=50)
# Fitting and predicting for test data
final_weekly.fit(x_train,y_train).predict(x_test)
Evaluation metric results for monthly datasetXG Boost algorithm is considered as final model for monthly dataset.
XG Boost algorithm is considered as final model for quarterly dataset.
8. Model Deployment:
Finalized model shown in previous section is considered for app deployment.
The predicted stocks are added with 10% of buffer to compensate for growth in the industry and the population. 
The Web API has been developed with the help of Flask framework and deployed in Heroku platform.
Screen-shots of the API is shown below
First Page: In first page of the API, the user has to select the type of inventory analysis i.e., weekly, monthly or quarterly.
First Page of the web APIAfter submitting the type of inventory analysis, next page will open with selected type. 
Sample second page, if the user select "weekly" is shown below
2nd Page when user selects type as weeklyResults Page : This page shows the result i.e., how much inventory should be present. 
The input from second page is processed and model will predict the result which is represented in results page.
The representation of second page is shown below.
Result pageThe result page has one more option of "Export to Excel". This option will take the input from 2nd page and export the result to the excel of all product type (i.e., 1 to 1115) with the respective predicted inventory.
Link of Web API : 
Inventory Management
Edit descriptionefficient-inventory.herokuapp.com
Git-hub link:
sumantha-NTS/Inventory-management-system
Contribute to sumantha-NTS/Inventory-management-system development by creating an account on GitHub.github.com
9. Conclusion:
Inventory management is a very tedious process if not done properly may lead to loss in sales, customer dissatisfaction etc. Smart retailers will use predictive analysis which will lead better management of stocks, centralized control which intern increase the productivity.
10. References: 
sklearn.preprocessing.MinMaxScaler - scikit-learn 0.24.2 documentation
Edit descriptionscikit-learn.org
Welcome to Flask - Flask Documentation (1.1.x)
Welcome to Flask's documentation. Get started with Installation and then get an overview with the Quickstart . There is…flask.palletsprojects.com
XGBoost Documentation - xgboost 1.5.0-SNAPSHOT documentation
XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable…xgboost.readthedocs.io
Documentation
Technical documentation that describes the Heroku platform.devcenter.heroku.com
