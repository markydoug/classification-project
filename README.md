# Classification Project

## Project Description
Companies all across the globe deal with customers leaving on a regular basis. These people are described as those who "churn". Telco is wondering, "Why are our customers leaving?" In this project I will look at data of their customers and identify drivers that might affect the chance a customer might churn.

## Project Goals
* Identify drivers of churn for Telco customers
* Use the identified drivers to develop a model to determine if a customer is likely to churn
* Churn is defined as a customer who has left Telco
* This information can be useful to help Telco find ways to retain customers who are likely to churn.

## Initial Thoughts

My initial hypothesis is that drivers of churn will be predictors of if a customer will churn in the near future.

## The Plan
* Aqcuire the data from Codeup mySQL database

* Prepare data
    * Remove duplicate columns (payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', )
    * Drop customers whose total_charges are spaces; these customers are new customers (tenure=0 and churn=No)
    * Encode churn as 'churn_encoded' {'Yes': 1, 'No': 0}, then drop 'churn' column

* Explore data in search of drivers of churn
    * Answer the following initial questions
        * What percentage of customers churn?
        * Does a customer's tenure affect churn?
        * Does the number of internet add-ons affect churn?
        * Does being a senior citizen affect churn?
        * Do higher monthly charges affect churn?
        * Do those who have a month-to-month contract churn more?

* Develop a model to predict if a customer will churn
    * Use drivers identified through exploration to build different predictive models
    * Evaluate models on train and validate data
    * Select best model base on highest recall (because saying they didn't churn and they churned is more costly)
    * Evaluate the best model on the test data

* Draw conclusions

## Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|feature 1| what is this telling us|
|feature 2| what is this saying|


## Steps to Reproduce
1. Clone this repo
2. Acquire the data from Codeup mySQL "telco" database
3. Put the data in the file containing the cloned repo.
4. Run notebook.

## Takeaways and Conclusions
* takeaway 1
* takeaway 2

## Recommendataions