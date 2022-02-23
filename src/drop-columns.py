#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sparkbyexamples.com

"""
#Pandas Drop Column(s) from DataFrame
import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df)

# Drops 'Fee' column
df2=df.drop(["Fee"], axis = 1)
print(df2)


# Explicitly using parameter name 'labels'
df2=df.drop(labels=["Fee"], axis = 1)
print(df2)

# Alternatively you can also use columns instead of labels.
df2=df.drop(columns=["Fee"], axis = 1)
print(df2)


# Drop column by index.
df2=df.drop(df.columns[[1]], axis = 1)
print(df2)


# using inplace=True
df.drop(df.columns[[1]], axis = 1, inplace=True)
print(df)

# Drop Two or More Columns By Label Name
df=pd.DataFrame(technologies)
df2=df.drop(["Courses", "Fee"], axis = 1)
print(df2)

#drop two or more columns by index
df2=df.drop(df.columns[[0,1]], axis = 1)
print(df2)

#Drop Columns from List of Columns
lisCol = ["Courses","Fee"]
df2=df.drop(lisCol, axis = 1)
print(df2)

#Remove Columns from a List of Columns (iteratively) By Condition.
for col in df.columns:
    if 'Fee' in col:
        del df[col]
print(df)

# Using df.loc() to Remove Columns Between Specified Columns
df.drop(df.loc[:, 'Courses':'Fee'].columns, axis = 1, inplace=True)
print(df)

#Using df.iloc() to Remove Columns Between Specified Column Indexes.
df.drop(df.iloc[:, 1:2], inplace=True, axis=1)
print(df)














