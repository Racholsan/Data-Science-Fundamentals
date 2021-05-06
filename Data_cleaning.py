# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:44:40 2021

@author: Racholsan
"""


# importing pandas library
import pandas as pd

# reading the csv file from working directory
data = pd.read_csv("C:/Users/Racholsan/Desktop/Python Files/archive/vehicles.csv")

# Remove duplicates
data.drop_duplicates(inplace = True)

# checking for any null values
data.isnull().any

# total count of null values in columns
data.isnull().sum()

# percentage of null values in columns
data.isnull().sum() / data.shape[0]

# remove null columns over a threshold
thresh = len(data)*0.6
data.dropna(thresh = thresh, axis =1)
data.dropna(thresh = thresh, axis =1).shape
data.dropna(thresh = 21, axis = 0).shape

# inputting null values
data.odometer.fillna(data.odometer.median()).isnull().any
data.odometer.fillna(data.odometer.mean()).isnull().any

# convert text to all lower or upper
data.description.head()
data.description.head().apply(lambda x: x.lower()).head()
data.description.head().apply(lambda x: x.upper()).head()

# to string
data.description.astype(str).apply(lambda x: x.lower())

# to float
data.cylinders.head()
data.cylinders.dtype
data.cylinders.value_counts()
data.cylinders = data.cylinders.apply(lambda x: str(x).lower().replace('cylinders', '').strip())

data.cylinders.value_counts()

# changing data type
data.cylinders = pd.to_numeric(data.cylinders, errors = 'coerce')
data.cylinders.value_counts()
data.cylinders.isnull().sum()
data.cylinders.fillna(data.cylinders.mean(), inplace = True)

# visualization
## boxplot
data.boxplot('odometer')
data.boxplot('price')
## histogram plot
data.hist('odometer')

numeric = data._get_numeric_data()

# removing the outliers
data_outliers = data[(data.price < data.price.quantile(0.995)) & (data.price > data.price.quantile(0.005))]

# visualization of columns in cleaned data
data_outliers.boxplot('price')
data_outliers.hist('price')
data_outliers = data[(data.odometer < data.odometer.quantile(0.995)) & (data.odometer > data.odometer.quantile(0.005))]
data_outliers.boxplot('odometer')

# histogram plot
data_outliers.hist('odometer')


# MinMax Scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(data.cylinders.values.reshape(-1, 1))

scaler.transform(data.cylinders.values.reshape(-1, 1))
scaler.fit_transform(data.cylinders.values.reshape(-1, 1))
