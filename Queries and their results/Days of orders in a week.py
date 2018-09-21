# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:32:13 2018

@author: KURAMS
"""

import pandas as pd

import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
color = sns.color_palette()

import warnings
warnings.filterwarnings('ignore')

order_products_prior_df= pd.read_csv("./input/order_products_prior.csv")
order_products_train_df= pd.read_csv("./input/order_products_train.csv")
orders_df= pd.read_csv("./input/orders.csv")
products_df= pd.read_csv("./input/products.csv")

order_products_all = pd.concat([order_products_train_df, order_products_prior_df], axis=0)

grouped = orders_df.groupby("order_id")["order_dow"].aggregate("sum").reset_index()
grouped = grouped.order_dow.value_counts()

f, ax = plt.subplots(figsize=(10, 10))
sns.barplot(grouped.index, grouped.values)
plt.ylabel('Number of orders', fontsize=13)
plt.xlabel('Days of order in a week', fontsize=13)
plt.show()