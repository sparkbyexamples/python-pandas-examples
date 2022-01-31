import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,22000,24000],
    'Duration':['30day','40days','35days','40days','60days'],
    'Discount':[1000,2300,1200,2500,2000]
              }
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=index_labels)
print(df)

# Select single Row
print(df.loc['r2'])

# Select Single Column by label
print(df.loc[:, "Courses"])

# Select Multiple Rows by Label
print(df.loc[['r2','r3']])

# Select Multiple Columns by labels
print(df.loc[:, ["Courses","Fee","Discount"]])

# Select Rows Between two Index Labels
# Includes both r1 and r4 rows
print(df.loc['r1':'r4'])

# Select Columns between two Labels
# Includes both 'Fee' and 'Discount' columns
print(df.loc[:,'Fee':'Discount'])

# Select Alternate rows By indeces
print(df.loc['r1':'r4':2])

# Select Alternate Columns between two Labels
print(df.loc[:,'Fee':'Discount':2])

# Using Conditions
print(df.loc[df['Fee'] >= 24000])