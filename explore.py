import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats


###################################################################################
################################## EXPLORE DATA ###################################
###################################################################################

def split_churn(train):
    #split data for exploration into a dataframe that shows all info on those who churned
    train_churn = train[train.churn_encoded == 1]

    #and a dataframe that show all info on those who didn't churn
    train_no_churn = train[train.churn_encoded == 0]

    return train_churn, train_no_churn

def churn_percentage(train):
    #split data for plotting
    train_churn, train_no_churn = split_churn(train)

    values = [len(train_churn.churn_encoded), len(train_no_churn.churn_encoded)] 
    labels = ["Churn", "Didn't Churn"] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Churned Customers Represent 27% of the train data')
    plt.show()

def tenure_viz(train):
    #split data for plotting
    train_churn, train_no_churn = split_churn(train)
    
    #plot boxenplot to compare tenure with churn
    average = train["tenure"].mean()
    sns.boxenplot(data=train, x='churn_encoded', y="tenure", palette='pastel', saturation=1)
    plt.xlabel(xlabel="Did they churn? \n0 = No, 1 = Yes")
    plt.ylabel(ylabel="Tenure (Months as a customer)")
    plt.title("Does a customer's tenure affect churn? ")
    plt.axhline(average, ls='--', color='black', label='Mean tenure') 
    plt.legend(loc='upper center')
    plt.show()
    
    #plot churn and no churn histogram on top of each other
    train_no_churn['tenure'].hist(label = "Didn't churn", color='#c0d6e4')
    train_churn['tenure'].hist(label = "Churned", color='#ffc3a0')
    plt.ylabel(ylabel='Number of customers')
    plt.xlabel(xlabel="Months as a customer (tenure)")
    plt.legend(loc='upper center')
    plt.show()

def monthly_charges_viz(train):
    #split data for plotting
    train_churn, train_no_churn = split_churn(train)

    #plot boxenplot to compare monthly charges with churn
    average = train["monthly_charges"].mean()
    sns.boxenplot(data=train, x='churn_encoded', y="monthly_charges", palette='pastel', saturation=1)
    plt.title("Does a customer's monthly charges affect churn? ")
    plt.axhline(average, ls='--', color='black', label= 'Mean Monthly charges') 
    plt.xlabel(xlabel="Did they churn? \n0 = No, 1 = Yes")
    plt.legend(loc='upper center')
    plt.show()