"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-drop-row-from-dataframe

"""

#Pandas Drop Rows From DataFrame Examples

import pandas as pd
import numpy as np

technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python"],
    'Fee' :[20000,25000,26000,22000],
    'Duration':['30day','40days',np.nan, None],
    'Discount':[1000,2300,1500,1200]
               }

indexes=['r1','r2','r3','r4']
df = pd.DataFrame(technologies,index=indexes)
print(df)

# Drop rows by Index Label
df = pd.DataFrame(technologies,index=indexes)
df1 = df.drop(['r1','r2'])
print(df1)

# Delete Rows by Index Labels
df1 = df.drop(index=['r1','r2'])
print(df1)

# Delete Rows by Index Labels & axis
df1 = df.drop(labels=['r1','r2'])
print(df1)

df1 = df.drop(labels=['r1','r2'],axis=0)
print(df1)

# Delete Rows by Index numbers
df = pd.DataFrame(technologies,index=indexes)
df1=df.drop(df.index[[1,3]])
print(df1)

# Removes First Row
df=df.drop(df.index[0])
print(df)

# Delete Rows by Index Range
df = pd.DataFrame(technologies,index=indexes)
df1=df.drop(df.index[2:])
print(df1)

# Remove rows when you have default index.
df = pd.DataFrame(technologies)
df1 = df.drop(0)
print(df1)

# Remove rows when you have default index.
df = pd.DataFrame(technologies)
df3 = df.drop([0, 3])
print(df3)

# Remove rows when you have default index.
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df4 = df.drop(range(0,2))
print(df4)

# Delete Rows inplace
df = pd.DataFrame(technologies,index=indexes)
df.drop(['r1','r2'],inplace=True)
print(df)

# Delete Rows by Checking Conditions
df = pd.DataFrame(technologies)
df1 = df.loc[df["Discount"] >=1500 ]
print(df1)

# Delete rows with Nan, None & Null Values
df = pd.DataFrame(technologies,index=indexes)
df2=df.dropna()
print(df2)





















