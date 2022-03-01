"""
@author: sparkbyexamples.com

"""
#Pandas Concat Two DataFrames Explained
#create DataFrames

import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900]})


# Using pandas.concat() to concat two DataFrames
data = [df, df1]
df2 = pd.concat(data)
print(df2)


# Use pandas.concat() method to ignore_index 
df2 = pd.concat([df, df1], ignore_index=True, sort=False)
print(df2)

#Using pandas.concat() to Join Two DataFrames on columns
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","pandas"],
                      'Fee' :[20000,25000,22000,24000]})
  
df1 = pd.DataFrame({'Duration':['30day','40days','35days','60days'],
                      'Discount':[1000,2300,2500,2000,]}) 

#  Using pandas.concat() to join concat two DataFrames
df2 = pd.concat([df, df1], axis=1, join='inner')
print(df2)


#Concatenate Multiple DataFrames Using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark", "PySpark", "Python", "Pandas"],
                    'Fee' : ['20000', '25000', '22000', '24000']}) 
  
df1 = pd.DataFrame({'Courses': ["Unix", "Hadoop", "Hyperion", "Java"],
                    'Fee': ['25000', '25200', '24500', '24900']})
  
df2 = pd.DataFrame({'Duration':['30day','40days','35days','60days','55days'],
                    'Discount':[1000,2300,2500,2000,3000]})
  
# Appending multiple DataFrame
df3 = pd.concat([df, df1, df2])
print(df3)

#Use DataFrame.append() to Concat Two DataFrames

import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900]})


# Using DataFrame.append() to concat Two DataFrames
df2 = df.append(df1)
print(df2)


# Use DataFrame.append() 
df2 = df.append(df1, ignore_index=True)
print(df2)



