# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:46:16 2021

@author: Racholsan
"""

"""
What is Pandas ?

Pandas: pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

Why to use Pandas ?

- Pandas uses dataframes and series that we can use to explore, manipulate and cleaning rows and columns
- Pandas can also be used for quick visualization purposes

"""
# importing the pandas library 
import pandas as pd

# pandas reading the csv file 
data = pd.read_csv("C:/Users/Racholsan/Desktop/Python Files/archive/vehicles.csv")

# shape of data (rows * columns)
data.shape

# returns the first x number of rows when head(num). Without a number it returns 5
data.head()

# returns the last x number of rows when tail(num). Without a number it returns 5
data.tail()

# returns an object with all of the column headers 
data.columns

# basic information on all columns 
data.info()

# gives basic statistics on numeric columns
data.describe()

# shows what type the data was read in as (float, int, string, bool, etc.)
data.dtypes

# shows which columns have null values
data.isnull().any()

# summation of null values in columns
data.isnull().sum()

# checking for null values (% of nulls)
data.isnull().sum() / data.shape[0]

# for categorical variables 

# shows the values in columns
data.type

# shows unique values which appeared in column
data.type.unique()

# shows the counts for those unique values 
data.type.value_counts()


# shows the percentage value of types
data.type.value_counts() / data.type.notnull().sum()

################################## Graphs ####################################
# histogram of year
data.year.plot(kind = 'hist')

data.year.hist()

data.year.hist(bins = 50)

data.year.hist()
data.year.hist(bins = 50)

# bar chart of types
data.type.value_counts().plot(kind = 'bar')







