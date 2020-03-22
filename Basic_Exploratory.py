#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from IPython.display import display


# Create table for missing data analysis
def draw_missing_data_table(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    display(missing_data)

def cut_levels(x, threshold, new_value):
    value_counts = x.value_counts()
    labels = value_counts.index[value_counts < threshold]
    x[np.in1d(x, labels)] = new_value
    return labels

def cut_levels_new(x, threshold, new_value):
    x = x.copy()
    value_counts = x.value_counts()
    labels = value_counts.index[value_counts < threshold]
    x[np.in1d(x, labels)] = new_value
    return x, labels

def find_outliers(Data, col)
    data_mean, data_std = np.mean(Data[col]), np.std(Data[col])
    cut_off = data_std * 4
    lower, upper = data_mean - cut_off, data_mean + cut_off
    return Data.loc[(Data[col]<lower) | (Data[col]>upper), col ] #.index

def basic_eda(df):
    print("----------HEAD--------")
    display(df.head(5));
    print("----------INFO-----------------")
    display(df.info() )
    print("----------Describe-------------")
    display(df.describe())
    print("----------Columns--------------")
    display(df.columns)
    print("----------Data Types-----------")
    display(df.dtypes)
    print("-------Missing Values----------")
    display(df.isnull().sum().loc[lambda x: x>0])
    print("-------NULL values-------------")
    display(df.isna().sum().loc[lambda x: x>0])
    print("-----Shape Of Data-------------")
    display(df.shape)
    print("-----Sample-------------")
    display(df.sample(5))
    print("******  Counts  ******* \n")
    for c in df.columns[:(min(df.columns.shape[0],10))]:
        print("---- %s ---" % c)
        display(df[c].value_counts().to_frame())
#     display(df.apply(lambda x: x.value_counts() , axis = 0).T.stack().to_frame() )

def Look_Date(data):
    print("The data starts from the date {} and ends in {}".format(data.min().date(),data.max().date()))
    print("So we have {} of data".format(data.max().date()-data.min().date()))

