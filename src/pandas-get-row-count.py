"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-get-the-number-of-rows

"""

#Pandas Get the Number of Rows
#createDataFrame

import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Courses Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df = pd.DataFrame(technologies)
print(df)
print(df.index)

#Get number of rows in DataFrame
print('Row count is:', len(df.index))

print('Row count is:', len(df))

#Get Row Count in DataFrame Using .len(DataFrame.axes[0]) Method
print(df.axes)

print(df.axes[0])

print('Row count is:', len(df.axes[0]))

#Using df.shape[0] to Get Rows Count

df = pd.DataFrame(technologies)
row_count = df.shape[0]  
print(row_count)

col_count = df.shape[1]  
print(col_count)

#Using df.count method
rows_count = df.count()[0]
rows_count =  df[df.columns[0]].count()
print('Number of Rows count is:', rows_count )














