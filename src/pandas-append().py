"""
@author: sparkbyexamples.com

"""
#Pandas append() Usage by Examples
#create dataframe

import pandas as pd

df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900],
                    'Duration': ['30days','35days','40days','45days']})

# Using append() method
df2 = df.append(df1)
print(df2)


# Using append() with ignore_index
df2 = df.append(df1, ignore_index=True)
print(df2)


# Append Dict as row to DataFrame
new_row = {'Courses':'Hyperion', 'Fee':24000}
df2=df.append(new_row, ignore_index=True)
print(df2)

# Create third DataFrame  
df2 = pd.DataFrame({'Courses':['PHP','GO'],
                    'Duration':['30day','40days'],
                    'Fee':[10000,23000]})
  
# Appending multiple DataFrame
df3 = df.append([df1, df2], ignore_index=True)
print(df3)


