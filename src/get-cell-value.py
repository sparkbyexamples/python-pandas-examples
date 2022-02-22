"""
@author: sparkbyexamples.com

"""

#Pandas – How to Get a Cell Value From DataFrame?

import pandas as pd
technologies = {
     'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
     'Fee' :[24000,25000,25000,24000,24000],
     'Duration':['30day','50days','55days', '40days','60days'],
     'Discount':[1000,2300,1000,1200,2500]
          }
df = pd.DataFrame(technologies)
print(df)

# Using DataFrame.loc[] Get cell value by name & index
df2=df.loc[3]['Duration']
print(df2)

df2=df.loc[3,'Duration']
print(df2)

df2=df.loc[3][2]
print(df2)

# Using DataFrame.iloc[] Get cell value by index & name
df2=df.iloc[3]['Duration']
print(df2)

df2=df.iloc[3][2]
print(df2)

df2=df.iloc[3,2]
print(df2)

# Using DataFrame.at[]
df2=df.at[3,'Duration']
print(df)

df2=df.at[df.index[3],'Duration']
print(df2)

# Using DataFrame.iat[]
df2=df.iat[3,2]
print(df2)


#Get a cell value
df2=df["Duration"].values[3]
print(df2)


# Get cell value from last row
df2=df.iloc[-1,2]
print(df2)


df2=df.iloc[-1]['Duration']
print(df2)


df2=df.at[df.index[-1],'Discount']
print(df2)                








