#Ignore Warnings
import warnings 
warnings.filterwarnings("ignore")

#Acquire
from env import host, username, password
from pydataset import data

#Imports for the acquire file
import pandas as pd 
import numpy as np
import os

os.path.isfile('zillow_df.csv')

def acquire_zillow():
    '''
    Obtain the zillow data of single unit properties during May - August 2017
    '''
    sql_query = '''select *
    from  properties_2017
    join predictions_2017 using(parcelid)
    where transactiondate between "2017-05-01" and "2017-08-31"
        and propertylandusetypeid between 260 and 266
            or propertylandusetypeid between 273 and 279
            and not propertylandusetypeid = 274
        and unitcnt = 1;
    '''
    connection = f'mysql+pymysql://{username}:{password}@{host}/zillow'
    df = pd.read_sql(sql_query, connection)
    return df