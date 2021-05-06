# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:22:44 2021

@author: Racholsan
"""

# importing pandas library
import pandas as pd

data = pd.read_csv("C:/Users/Racholsan/Desktop/Python Files/archive/vehicles.csv")

data2 = data.head(100)

# view and rename columns
data.columns
data.rename(index = str, columns = {'state':'new_state'}, inplace = True)
data.rename(index = str, columns = {'new_state':'state'}, inplace = True)

# Single column selection
data['state']

# view all the columns from selected group of rows
data[0:100]

# selecting multiple columns
url_state_price = data[['url', 'state', 'price']]

# filtering multiple columns
url_state_price2 = data.loc[:, ['url', 'state', 'price']]
url_state_price2 = data.loc[0:100, ['url', 'state', 'price']]
url_state_price3 = data.iloc[0:100, 0:3]

# dropping a single column
data_no_url = data.drop('url', axis = 1)

data_no_url_state = data.drop(['url', 'state'], axis = 1)

# Column creatiion
data["age"] = 2021 - data["year"]

# Column creation
data["current_year"] = 2021

# New cars age <= 4. Filtering by this criteria
data_new_cars = data[data.age <= 4]

data_new_cars_price = data[(data.age <= 4) | (data.price > 5000)]

# Filtering data by columns and boolean indexing
data.loc[data.age <= 2, :]


# new feature creation
data['price_per_mile'] = data['price'] / data['odometer']

#apply functiions
def price2x(x):
    return x*2
data['price2'] = data['price'].apply(price2x)


data.price.head()

data.price2.head()

data['price3'] = data.price.apply(lambda x: x*3)
data.price3.head()

# ternary operator & numeric to category conversion
data['isexpensive'] = data.price.apply(lambda x: 'expensive' if x > 10000 else 'cheap')
data.isexpensive.head(100).value_counts()

data['new_and_cheap'] = data.apply(lambda x: 'yes' if x['price'] < 10000 and x['age'] < 10 else 'no', axis = 1)
data['new_and_cheap'].head(100)

data['new_and_cheap'].head(100).value_counts()

# quantile and bins
data['price_quintile'] = pd.qcut(data.price, 5)
data['price_quintile'].value_counts()
pd.cut(data.price, 5).value_counts()

# dummy variable
dummie_var = pd.get_dummies(data[['price', 'year', 'fuel', 'transmission', 'type']].head(1000))

# pivot tables
pd.pivot_table(data, index = 'year', columns = 'type', values = 'price', aggfunc = 'mean')
pd.pivot_table(data, index = 'year', columns = 'type', values = 'price', aggfunc = 'mean').sort_index(ascending = False)
pd.pivot_table(data, index = 'year', columns = 'type', values = 'price', aggfunc = 'count').sort_index(ascending = False)
pd.pivot_table(data, index = 'year', columns = 'type', values = 'price', aggfunc = 'count').sort_index(ascending = False).plot()


#group by
grouped_data = data.groupby(['type', 'year']).mean()
grouped_data = data.groupby(['type', 'year'], as_index = False).mean()

# pd.merge == sql join
df1 = data[['url', 'state']]
df2 = data[['url', 'price']]
df_joined = pd.merge(df1, df2, on = 'url')


# appending
sample1 = data.sample(100, random_state = 1)
sample2 = data.sample(100, random_state = 2)
sample1.append(sample2)


# write to csv
data.head(1000).to_csv('top1000.csv')
