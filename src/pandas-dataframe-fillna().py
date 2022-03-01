"""
@author: sparkbyexamples.com

"""
#pandas.DataFrame.fillna() – Explained by Examples

# Create DataFrame
import pandas as pd
import numpy as np
df = pd.DataFrame(({
     'Courses':["Spark",'Java',"Scala",'Python'],
     'Fee' :[20000,np.nan,26000,24000],
     'Duration':['30days','40days','NA','40days'],
     'Discount':[1000,np.nan,2500,None]
               }))
print(df)


# fillna to replace all NaN
df2=df.fillna('None')
print(df2)


# fillna on one column
df2['Discount'] =  df['Discount'].fillna('0')
print(df2)


# fillna() on multiple columns
df2[['Discount','Fee']] =  df[['Discount','Fee']].fillna('0')
print(df2)


# fillna() on multiple columns
df2 =  df.fillna(value={'Discount':'0','Fee':10000})
print(df2)


# fill with limit
df2=df.fillna(value={'Discount':0,'Fee':0},limit=1)
print(df2)




