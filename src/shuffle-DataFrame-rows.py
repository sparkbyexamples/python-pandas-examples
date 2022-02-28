"""
@author: sparkbyexamples.com

"""

#Pandas Shuffle DataFrame Rows Examples
# Create a DataFrame with a Dictionary of Lists

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
df = pd.DataFrame(technologies)
print(df)


# shuffle the DataFrame rows & return all rows
df1 = df.sample(frac = 1)
print(df1)


# Create a new Index starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)


# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)


# Using numpy.random.shuffle to Change Order of Rows
import numpy as np
# Using numpy permutation() method to shuffle DataFrame rows
df1 = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
print(df1)


# Using sklearn to shuffle rows
from sklearn.utils import shuffle
df = shuffle(df)


# Using apply() method to shuffle the DataFrame rows
import numpy as np
df1 = df.apply(np.random.permutation, axis=1)    
print(df1)


# Using lambda method to Shuffle/permutating DataFrame rows
df2 = df.apply(lambda x: x.sample(frac=1).values)
print(df2)


# Using sample() method to shuffle DataFrame rows and columns
df2 = df.sample(frac=1, axis=1).sample(frac=1).reset_index(drop=True)
print(df2)





