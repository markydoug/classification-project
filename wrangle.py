import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import env

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy import stats


###################################################################################
#################################### ACQUIRE DATA #################################
###################################################################################
def get_db_url(db, user=env.username, password=env.password, host=env.host):
    '''
    This function uses the imported host, username, password from env file, 
    and takes in a database name and returns the url to access that database.
    '''

    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df.
    '''
    # Create SQL query.
    sql_query = '''
                SELECT * 
                FROM customers
                JOIN contract_types USING (contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN payment_types USING (payment_type_id)
                '''
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url(db = 'telco_churn'))

    return df


#function to go get customer data from the telco_churn database
def get_telco_data():
    '''Checks to see if there is titanic data locally stored
    if none is there it will go get the telco data, return it
    as a dataframe and then save it as csv file.'''
    
    filename = 'telco.csv'
   
    #if cached file exists use it
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
   
    #else go get the data
    else:
        df = new_telco_data()
        df.to_csv(filename,index=False)
        
    return df

###################################################################################
##################################### PREP DATA ###################################
###################################################################################

def prep_telco(df):
    '''Prepares acquired teclo data for exploration'''

    df.drop_duplicates(inplace=True)
    df = df[df.total_charges!=' ']
    df.total_charges = df.total_charges.astype(float)
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    df.drop(columns=['customer_id','payment_type_id', 'internet_service_type_id','contract_type_id', 'churn'], inplace=True)
    
    return df


###################################################################################
#################################### SPLIT DATA ###################################
###################################################################################

def train_validate_test_split(df, target):
    '''
    Takes in a data frame and the target variable column  and returns
    train (75%), validate (15%), and test (10%) data frames.
    '''
    train, test = train_test_split(df,test_size = 0.1, stratify = df[target], random_state=27)
    train, validate = train_test_split(train, test_size = 0.166666666666, stratify = train[target],random_state=27)
    
    return train, validate, test

def prep_for_model(train, validate, test, target):
    '''
    Takes in train, validate, and test data frames
    then splits  for X (all variables but target variable) 
    and y (only target variable) for each data frame
    '''
    drop_columns = list(train.select_dtypes(exclude=np.number).columns) + [target]

    X_train = train.drop(columns=drop_columns)
    y_train = train[target]

    X_validate = validate.drop(columns=drop_columns)
    y_validate = validate[target]

    X_test = test.drop(columns=drop_columns)
    y_test = test[target]

    return X_train, y_train, X_validate, y_validate, X_test, y_test

def prep_df_for_model(df, target):
    '''
    Takes in a data frame and the target variable column, splits the data
    into train (80%), validate (15%), and test (10%) data frames
    then splits again for X (all variables but target variable) and 
    y (only target variable) for each data frame
    '''
    
    train, validate, test = train_validate_test_split(df, target)

    X_train, y_train, X_validate, y_validate, X_test, y_test = prep_for_model(train, validate, test, target)

    return X_train, y_train, X_validate, y_validate, X_test, y_test