"""
@author: sparkbyexamples.com
For complete examples refer 
https://sparkbyexamples.com/pandas-drop-row-on-column-value-usage-with-example

"""
# Create pandas DataFrame
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python"],
    'Fee' :[22000,25000,np.nan,24000],
    'Duration':['30day',None,'55days',np.nan],
    'Discount':[1000,2300,1000,np.nan]
          }
df = pd.DataFrame(technologies)
print(df)

df.drop(df[df['Fee'] >= 24000].index, inplace = True)
print(df)

# Remove row
df = pd.DataFrame(technologies)
df2 = df[df.Fee >= 24000]
print(df2)

#Using loc[]
df=pd.DataFrame(technologies)
df2 = df.loc[df["Fee"] >= 24000 ]
print(df2)

# Delect rows based on multiple column value
df = pd.DataFrame(technologies)
df = df[ (df['Fee'] >= 22000) & (df['Discount'] == 2300)]
print(df)

# Drop rows with None/NaN values
df=pd.DataFrame(technologies)
df2 = df[df.Duration.notnull()]
print(df2)


# Delete rows using DataFrame.query()
df2=df.query("Courses == 'Spark'")
print(df)

#Using variable
value='Spark'
df2=df.query("Courses == @value")
print(df2)

#Not equals, in & multiple conditions
df=pd.DataFrame(technologies)
df2=df.query("Courses != 'Spark'")
print(df2)


#Not equals, in & multiple conditions
df2=df.query("Courses in ('Spark','PySpark')")
print(df2)


# Other ways to Delete Rows
df2=df.loc[df['Courses'] == value]
print(df2)


# Other ways to Delete Rows
df2=df.loc[df['Courses'] != 'Spark']
print(df2)


# Delect rows based on inverse of column values
df=pd.DataFrame(technologies)
df1 = df[~(df['Courses'] == "PySpark")].index 
df.drop(df1, inplace = True)
print(df)











