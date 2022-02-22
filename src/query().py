"""
@author: sparkbyexamples.com
"""
#Pandas.DataFrame.query() by Examples
import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df = pd.DataFrame(technologies)
print(df)
# Query all rows with Courses equals 'Spark'
df2=df.query("Courses == 'Spark'")
print(df2)
# Query Rows by using Python variable
value='Spark'
df2=df.query("Courses == @value")
print(df2)
# Replace current esisting DataFrame
df=pd.DataFrame(technologies)
df2=df.query("Courses == 'Spark'",inplace=True)
print(df2)
# not equals condition
df=pd.DataFrame(technologies)
df2=df.query("Courses != 'Spark'")
print(df2)
# Query Rows by list of values
print(df.query("Courses in ('Spark','PySpark')"))
# Query Rows by list of values
values=['Spark','PySpark']
print(df.query("Courses in @values"))
# By using lambda function
print(df.apply(lambda row: row[df['Courses'].isin(['Spark','PySpark'])]))
# Other examples you can try to query rows
df2=df.loc[(df['Discount'] >= 1000) & (df['Discount'] <= 2000)]
print(df2)
df2=df.loc[(df['Discount'] >= 1200) & (df['Fee'] >= 23000 )]
print(df2)




