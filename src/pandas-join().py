"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-join()-method-explained-with-examples

"""

#Pandas Join Explained With Examples
#create DataFrames
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)


# pandas join 
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)


# pandas Inner join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)


# pandas Right join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)


# pandas outer join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='outer')
print(df3)


# pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
print(df3)


# pandas join
df3=df1.join(df2.set_index('Courses'), how='inner', on='Courses')
print(df3)


