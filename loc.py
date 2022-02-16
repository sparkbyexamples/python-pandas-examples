#Pandas Select Rows by Index Label
"""
@author: sparkbyexamples.com

"""
# Use pandas.DataFrame.loc[] to Select Rows by Index Labels
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days',np.nan,None,'55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
index_labels=['r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=index_labels)
print(df)
# Select Row by Index Label
print(df.loc['r2'])
# Select Rows by Index Label List
print(df.loc[['r2','r3','r6']])
# Select Rows by Label Index Range
print(df.loc['r1':'r5'])
# Select Alternate Rows with in Index Labels
print(df.loc['r1':'r5':2])

