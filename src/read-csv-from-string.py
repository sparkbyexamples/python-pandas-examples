#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sparkbyexamples.com
"""

import pandas as pd
from io import StringIO

csvString = """Spark,25000,50 Days,2000
Pandas,20000,35 Days,1000
Java,15000,,800
Python,15000,30 Days,500
PHP,18000,30 Days,800"""

# Read from CSV String
csvStringIO = StringIO(csvString)
df = pd.read_csv(csvStringIO, sep=",", header=None)
print(df)

# With columns
csvStringIO = StringIO(csvString)
columns=['Course','Fee','Duration','Discount']
df = pd.read_csv(csvStringIO, sep=",", header=None,names=columns)
print(df)

# Ignore Header and assign column names
df = pd.DataFrame([row.split(',') for row in csvString.split('\n')], columns=columns)
print(df)

# Read from clipboard
df = pd.read_clipboard(sep=',')
print(df)