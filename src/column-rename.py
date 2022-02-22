"""
@author: sparkbyexamples.com

"""

#Pandas rename Column with example

import pandas as pd
technologies = ({
  'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
  'Fee' :[20000,25000,26000,22000,24000,21000,22000],
  'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
df2=df.columns
print(df2)


# Rename a Single Column 
df2=df.rename(columns = {'Courses':'Courses_List'})
print(df2.columns)


# Alternatively you can write above using axis
df2=df.rename({'Courses':'Courses_List'}, axis=1)
print(df2.columns)

# Alternatively you can write above using axis
df2=df.rename({'Courses':'Courses_List'}, axis='columns')
print(df2.columns)


# Rename multiple columns
df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
print(df.columns)


# pandas rename column by index
df2=df.columns.values[2] = "Courses_Duration"
print(df2)


#Rename columns wiht list
column_names = ['Courses','Fee','Duration']
df.columns = column_names
print(df.columns)

   
# Rename multiple columns
df.rename(columns = {'Courses':'Courses_List','Fee':'Courses_Fee', 
   'Duration':'Courses_Duration'}, inplace = True)
df2=df.columns
print(df2)


# Change to all lower case
df = pd.DataFrame(technologies)
df2=df.rename(str.lower, axis='columns')
print(df2.columns)


# Change to all upper case
df = pd.DataFrame(technologies)
df2=df.rename(str.upper, axis='columns')
print(df2.columns)


# Change column name using String.replace()
df.columns = df.columns.str.replace("Fee","Fee_Cost")
print(df.columns)



# Rename all column names
df.columns = df.columns.str.replace("_"," ")
print(df.columns)


# Throw Error when Rename column doesn't exists.
df2=df.rename(columns = {'Cour':'Courses_List'}, errors = "raise")
print(df2.columns)

















