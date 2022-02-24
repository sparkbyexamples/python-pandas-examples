"""

@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-apply()-function-usage-with-example

"""

#Pandas apply() Function to Single & Multiple Column(s)
import pandas as pd
import numpy as np
data = [(3,5,7), (2,4,6),(5,8,9)]
df = pd.DataFrame(data, columns = ['A','B','C'])
print(df)


# Using apply function single column
def add_4(x):
   return x+4
df["B"] = df["B"].apply(add_4)
print(df)


# Using Dataframe.apply() to apply function add column
df = pd.DataFrame(data, columns = ['A','B','C'])
print(df)
def add_3(x):
   return x+3
df2 = df.apply(add_3)
print(df2)


# apply() function on selected list of multiple columns
df = pd.DataFrame(data, columns = ['A','B','C'])
df[['A','B']] = df[['A','B']].apply(add_3)
print(df)


# apply a lambda function to each column
df = pd.DataFrame(data, columns = ['A','B','C'])
df2 = df.apply(lambda x : x + 10)
print(df2)


# Using Dataframe.apply() and lambda function
df = pd.DataFrame(data, columns = ['A','B','C'])
df["A"] = df["A"].apply(lambda x: x-2)
print(df)


# Using DataFrame.transform() 
df=pd.DataFrame(data,columns=['A','B','C'])
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)


# Using DataFrame.map() to Single Column
df=pd.DataFrame(data,columns=['A','B','C'])
df['A'] = df['A'].map(lambda A: A/2.)
print(df)


# Using DataFrame.assign() and Lambda
df=pd.DataFrame(data,columns=['A','B','C'])
df2 = df.assign(B=lambda df: df.B/2)
print(df2)


# Using Dataframe.apply() & [] operator
df=pd.DataFrame(data,columns=['A','B','C'])
df['A'] = df['A'].apply(np.square)
print(df)


# Using numpy.square() and [] operator
df=pd.DataFrame(data,columns=['A','B','C'])
df['A'] = np.square(df['A'])
print(df)



# Apply function NumPy.square() to square the values of two rows 
df=pd.DataFrame(data,columns=['A','B','C'])
df2 = df.apply(lambda x: np.square(x) if x.name in ['A','B'] else x)
print(df2)










