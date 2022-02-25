"""
@author: sparkbyexamples.com

"""
#Pandas Iterate Over Rows With Example
#create DataFrame
import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df)


# Iterate all rows using DataFrame.iterrows()
for index, row in df.iterrows():
    print (index,row["Fee"], row["Courses"])
    
    
# Row contains the column name and data
row = next(df.iterrows())[1]
print("Data For First Row:")
print(row)

# Iterate all rows using DataFrame.itertuples()
for row in df.itertuples(index = True):
    print (getattr(row,'Index'),getattr(row, "Fee"), getattr(row, "Courses"))


# Display one row from iterator
row = next(df.itertuples(index = True,name='Tution'))
print(row)

# Another alternate approach by using DataFrame.apply()
print(df.apply(lambda row: str(row["Fee"]) + " " + str(row["Courses"]), axis = 1))


# Using DataFrame.index
for idx in df.index:
     print(df['Fee'][idx], df['Courses'][idx])


# Another alternate approach byusing DataFrame.loc()
for i in range(len(df)) :
  print(df.loc[i, "Fee"], df.loc[i, "Courses"])
  
  
# Another alternate approach by using DataFrame.iloc()
for i in range(len(df)) :
  print(df.iloc[i, 0], df.iloc[i, 2])
  
  
# Iterate over column by column using DataFrame.items()
for label, content in df.items():
    print(f'label: {label}')
    print(f'content: {content}', sep='\n')






    
