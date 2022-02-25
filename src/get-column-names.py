"""
@author: sparkbyexamples.com


"""
# Pandas get column names from dataframe
#create DataFrame
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


# Get the list of all column names from headers
column_headers = list(df.columns.values)
print("The Column Header :", column_headers)

# Get the list of all column names from headers
column_headers = df.columns.values.tolist()
print("The Column Header :", column_headers)


#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
print("The Column Header:",column_headers)

#Using list(df) to get the list of all Column Names
column_headers = list(df)
print("The Column Header:",column_headers)


# Dataframe show all columns sorted list
col_headers=sorted(df)
col_headers


# Get all Column Header Labels as List
for column_headers in df.columns: 
    print(column_headers)
    
    
# Get Column Headers Using the keys() Method
column_headers = df.keys().values.tolist()
print("The Column Header :", column_headers)

# Get all numeric columns
numeric_columns = df._get_numeric_data().columns.values.tolist()
numeric_columns


# Simple Pandas Numeric Columns Code
numeric_columns=df.dtypes[df.dtypes == "int64"].index.values.tolist()
numeric_columns



