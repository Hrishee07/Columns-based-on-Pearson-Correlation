# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:17:55 2020

@author: Hrisheekesh
"""
import pandas as pd
def pearson_correlation(data_set):
    #creating an list to store the column names of data type integer or float
    column_names = []
    for column in data_set.columns:
        #checking for columns of integer datatype
        if data_set[column].dtype == 'int64':
            column_names.append(column)
        #checking for columns of float datatype
        elif data_set[column].dtype == 'float64':
            column_names.append(column)
    #creating an list to store the pearson correlation values
    pearson_value = []
    #dictionary used to map column names with pearson correlation vales
    dict1 = {}
    for column in range(len(column_names)-1):
        #calculating pearson correlation for subsequent columns in column names list
        k = data_set[column_names[column]].corr(data_set[column_names[column + 1]], method = 'pearson')
        #print(k)
        #storing correlation values in a list
        pearson_value.append(k)
        for i in range(len(pearson_value)):
            #dictionary key, value mapping
            dict1[column_names[column+1]] = pearson_value[i]
            #considering upper bound column to be removed and finding the columns to be removed from the data set
            columns_to_delete = [key  for (key, value) in dict1.items() if value > 0.85]
    #print(dict)
    for column in data_set.columns:
        if column in columns_to_delete:
            #deleting columns with pearson correlation value higher than 0.85
            del data_set[column]
    print(data_set)
    data_set.to_csv("sample.csv", index = False)
    return column_names, pearson_value, columns_to_delete
#considering the dataset is of csv format       
#loading the dataset Note: Please pass your dataset below by keeping both files in same directory
g = pd.read_csv("sample.csv")
print(pearson_correlation(g))
