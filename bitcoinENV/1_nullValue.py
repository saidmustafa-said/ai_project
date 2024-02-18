
import pandas as pd

data = pd.read_csv("main.csv")

data.head()

data.isnull().sum(axis=1).sort_values(ascending=False)
'''
.isnull()  : return null data
.sum(axis=1) : return data in row view and axis=0 return in column wise
.sort_values(ascending=False) : sorts the data
'''

data.shape[0] # number of rows and 1 for columns

# import datetime
# datetime.datetime.utcfromtimestamp(1609459200000 / 1000)

