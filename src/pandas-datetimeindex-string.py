#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sparkbyexamples.com
"""

# Create Pandas DataFrame.
import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Spark"],
    'Fee' :[22000,25000,23000],
    'Duration':['30days','50days','35days']
          }
df = pd.DataFrame(technologies)
df.index = pd.date_range('20210101','20210103',freq='D')
print(df)
print(type(df.index))

# Example 1
print(pd.Series(df.index.format()))

# Example 2
print(df.index.strftime('%m/%d/%Y, %r'))

# Example 3
df.index = df.index.strftime('%m/%d/%Y, %r')
print(df)
print(type(df.index))

# Example 4
# Create column with date
df['date'] = pd.date_range('20210101','20210103',freq='D')

# Column date would be of type datetime64[ns]
print(df)
print(df.date.dtypes)









