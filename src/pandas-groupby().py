"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-groupby()-explained-with-examples

"""
#Pandas groupby() Explained With Examples

#create DataFrame
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)


# Use groupby() to compute the sum
df2 =df.groupby(['Courses']).sum()
print(df2)


# Group by multiple columns
df2 =df.groupby(['Courses', 'Duration']).sum()
print(df2)


# Add Row Index to the group by result
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)


# Drop rows that have None/Nan on group keys
df2=df.groupby(by=['Courses'], dropna=False).sum()
print(df2)


# Remove sorting on grouped results
df2=df.groupby(by=['Courses'], sort=False).sum()
print(df2)


# Sorting group keys on descending order
groupedDF = df.groupby('Courses',sort=False).sum()
sortedDF=groupedDF.sort_values('Courses', ascending=False)
print(sortedDF)


# Using apply() & lambda
df2=df.groupby('Courses').apply(lambda x: x.sort_values('Fee'))
print(df2)


# Groupby & multiple aggregations
result = df.groupby('Courses')['Fee'].aggregate(['min','max'])
print(result)



# Groupby multiple columns & multiple aggregations
result = df.groupby('Courses').aggregate({'Duration':'count','Fee':['min','max']})
print(result)




