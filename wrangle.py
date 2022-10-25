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