import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats


###################################################################################
################################## EXPLORE DATA ###################################
###################################################################################

def explore_uvar(df):
    print('------------------------------------')
    print('-----------NUMERICAL DATA-----------')
    explore_num_uvar(df)
    print('------------------------------------')
    print('---------CATEGORICAL DATA-----------')
    explore_cat_uvar(df)


def explore_num_uvar(df):
    '''
    Takes in a data frame and returns univarite stats for numerical data
    '''
    num_vars = list(df.select_dtypes(include=np.number).columns)
    for col in num_vars:
        print(col)
        print(df[col].describe())
        df[col].hist()
        plt.show()
        sns.boxplot(y=col, data=df)
        plt.show()

def explore_cat_uvar(df):
    '''
    Takes in a data frame and a list of categorical variables
    Returns univarite stats
    '''
    cat_vars = list(df.select_dtypes(exclude=np.number).columns)
    for col in cat_vars:
        print(col)
        print(df[col].value_counts())
        print(df[col].value_counts(normalize=True)*100)
        sns.countplot(x=col, data=df)
        plt.show()

def explore_bvar(df, target):
    print('------------------------------------')
    print('-----------NUMERICAL DATA-----------')
    explore_num_bvar(df, target)
    print('------------------------------------')
    print('---------CATEGORICAL DATA-----------')
    explore_cat_bvar(df, target)


def explore_num_bvar(df, target):
    '''
    Takes in a data frame, target variable, and a 
    list of numerical variables. Returns bivarite stats 
    '''
    num_vars = list(df.select_dtypes(include=np.number).columns)
    for col in num_vars:
        sns.barplot(x=target, y=target, data=df)
        rate = df[col].mean()
        plt.axhline(rate,  label = f'Overall Mean of {col}', linestyle='dotted', color='black')
        plt.legend()
        plt.show()

def explore_cat_bvar(df, target):
    '''
    Takes in a data frame, target variable, and a 
    list of categorical variables. Returns bivarite stats 
    '''
    cat_vars = list(df.select_dtypes(exclude=np.number).columns)
    for col in cat_vars:
        sns.barplot(x=col, y=target, data=df)
        rate = df[target].mean()
        plt.axhline(rate, label = f'Average {target} rate', linestyle='--', color='black')
        plt.legend()
        plt.show()