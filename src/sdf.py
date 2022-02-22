# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#create pandas dataframe with example
# Create pandas DataFrame from List
import pandas as pd
technologies = [ ["Spark",20000, "30days"], 
                 ["Pandas",25000, "40days"], 
               ]
df=pd.DataFrame(technologies)
print(df)

# Add Column & Row Labels to the DataFrame
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

# Create DataFrame from Dict
technologies = {
    'Courses':["Spark","Pandas"],
    'Fee' :[20000,25000],
    'Duration':['30days','40days']
              }
df = pd.DataFrame(technologies)
print(df)

# Create DataFrame with Index.
technologies = {
    'Courses':["Spark","Pandas"],
    'Fee' :[20000,25000],
    'Duration':['30days','40days']
              }
index_label=["r1","r2"]
df = pd.DataFrame(technologies, index=index_label)
print(df)

# Creates DataFrame from list of dict
technologies = [{'Courses':'Spark', 'Fee': 20000, 'Duration':'30days'},
        {'Courses':'Pandas', 'Fee': 25000, 'Duration': '40days'}]

df = pd.DataFrame(technologies)
print(df)

# Create pandas Series
courses = pd.Series(["Spark","Pandas"])
fees = pd.Series([20000,25000])
duration = pd.Series(['30days','40days'])

# Create DataFrame from series objects.
df=pd.concat([courses,fees,duration],axis=1)
print(df)

# Assign Index to Series
index_labels=['r1','r2']
courses.index = index_labels
fees.index = index_labels
duration.index = index_labels

# Concat Series by Changing Names
df=pd.concat({'Courses': courses,
              'Course_Fee': fees,
              'Course_Duration': duration},axis=1)
print(df)

# Create Empty DataFrame
df = pd.DataFrame()
print(df)

# Create Empty DataFraem with Column Labels
df = pd.DataFrame(columns = ["Courses","Fee","Duration"])
print(df)


