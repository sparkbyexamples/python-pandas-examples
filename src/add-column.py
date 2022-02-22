"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-add-column-to-dataframe

"""
#Pandas Add Column to DataFrame

import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[1000,2300,1000,1200,2500]
          }

df = pd.DataFrame(technologies)
print(df)

# Add new column to the DataFrame

tutors = ['William', 'Henry', 'Michael', 'John', 'Messi']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)

# Add a multiple columns to the DataFrame

MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 =df.assign(MNCComp = MNCCompanies,TutorsAssigned=tutors )
print(df2)

# Derive New Column from Existing Column

df = pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x: x.Fee * x.Discount / 100)
print(df2)

# Add a constant or empty value to the DataFrame.

df = pd.DataFrame(technologies)
df2=df.assign(A=None,B=0,C="")
print(df2)

# Add New column to the existing DataFrame

df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies
print(df)

# Derive a new column from existing column

df['Discount_Percent'] = df['Fee'] * df['Discount'] / 100
print(df)

# Add new column at the specific position

df = pd.DataFrame(technologies)
df.insert(0,'Tutors', tutors )
print(df)

# Add new column by mapping to the existing column

df = pd.DataFrame(technologies)
tutors = {"William":"Spark", "Henry":"PySpark", "Michael":"Hadoop","John":"Python", "Messi":"pandas"}
df['Tutors'] = tutors
print(df)









