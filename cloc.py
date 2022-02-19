#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sparkbyexamples.com

"""

#Pandas Select Columns by Name or Index
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark"],
    'Fee' :[20000,25000],
    'Duration':['30days','40days'],
    'Discount':[1000,2300]
              }
df = pd.DataFrame(technologies)
print(df)
#Using loc[] to Select Columns by Name
# Select Columns by labels
df2 = df[["Courses","Fee","Duration"]]
print(df2)

# Select Multiple Columns
df2 = df.loc[:, ["Courses","Fee","Discount"]]
print(df2)

# Select all columns between Fee an Discount columns
df2 = df.loc[:,'Fee':'Discount']
print(df2)

# Select from 'Duration' column
df2 = df.loc[:,'Duration':]
print(df2)

# Select from beginning and end at 'Duration' column
df2 = df.loc[:,:'Duration']
print(df2)

# Select every alternate column
df2 = df.loc[:,::2]
print(df2)
# Select Multiple Columns by Index Position

# Selected by column position
df2 = df.iloc[:,[1,2,3]]
print(df2)
# Select Columns by Position Range
# Select between indexes 1 and 3 (2,3)
df2 = df.iloc[:,1:3]
print(df2)
# Select From 2nd to end
df2 = df.iloc[:,1:]
print(df2)
# Select First Two Columns
df2 = df.iloc[:,:2]
print(df2)
#select first column
df2=df.iloc[:,:1]
print(df2)
#select last column
df2=df.iloc[:,-1:]
print(df2)
