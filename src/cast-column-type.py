"""
@author: sparkbyexamples.com
For complete examples refer to
https://sparkbyexamples.com/pandas-cast-column-type-usage-with-example

"""

#Different Ways to Change Data Type in pandas
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration ':['30day','40days','35days', '40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)


# Convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)


# Change All Columns to Same type
df = df.astype(str)
print(df.dtypes)


# Change Type For One or Multiple Columns
df = df.astype({"Fee": int, "Discount": float})
print(df.dtypes)

# Convert Data Type for All Columns in a List
df = pd.DataFrame(technologies)
cols = ['Fee', 'Discount']
df[cols] = df[cols].astype('float')
print(df[cols].dtypes)


# By using a loop
for col in ['Fee', 'Discount']:
    df[col] = df[col].astype('float')
print(df[col].dtypes)


#By using apply() & astype() together
df=df[['Fee', 'Discount']].apply(lambda x: x.astype('float'))
print(df.dtypes)


# Converts object types to possible types
df = pd.DataFrame(technologies)
df = df.infer_objects()
print(df.dtypes)


# Convert Fee and Discount to numeric types
df = pd.DataFrame(technologies)
df[['Fee', 'Discount']] =df [['Fee', 'Discount']].apply(pd.to_numeric)
print(df.dtypes)






