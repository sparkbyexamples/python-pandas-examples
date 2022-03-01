"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-merge-dataframes-explained-with-examples
"""
#Pandas Merge DataFrames Explained Examples
#create DataFrames

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)
print(df1)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
print(df2)


# Using pandas.merge()
df3= pd.merge(df1,df2)
print(df3)

# Using DataFrame.merge()
df3=df1.merge(df2)
print(df3)

# Merge DataFrames by Columns
df3=pd.merge(df1,df2, on='Courses')
print(df3)


# When column names are different
df3=pd.merge(df1,df2, left_on='Courses', right_on='Courses')
print(df3)


# Merge DataFrames by Index
df3 = pd.merge(df1,df2,left_index=True,right_index=True)
print(df3)


# Merge by left Join
df3=pd.merge(df1,df2, on='Courses', how='left')
print(df3)


# Merge by right Join
df3=pd.merge(df1,df2, on='Courses', how='right')
print(df3)


# Merge by outer Join
df3=pd.merge(df1,df2, on='Courses', how='outer')
print(df3)








