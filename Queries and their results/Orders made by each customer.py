# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 09:55:17 2018

@author: KURAMS
"""

import pandas as pd
import matplotlib.pyplot as plt# Matlab-style plotting
import seaborn as sns
color = sns.color_palette()

import warnings
warnings.filterwarnings('ignore')

order_products_prior_df= pd.read_csv("./input/order_products_prior.csv")
order_products_train_df= pd.read_csv("./input/order_products_train.csv")
orders= pd.read_csv("./input/orders.csv")
products_df= pd.read_csv("./input/products.csv")

order_products_all = pd.concat([order_products_train_df, order_products_prior_df], axis=0)

grouped = orders.groupby('user_id')['order_id'].apply(lambda x: len(x.unique())).reset_index()
grouped = grouped.groupby('order_id').aggregate("count")

sns.set_style("whitegrid")
f, ax = plt.subplots(figsize=(15, 12))
sns.barplot(grouped.index, grouped.user_id)
plt.ylabel('Numbers of Customers')
plt.xlabel('Number of Orders per customer')
plt.xticks(rotation='vertical')
plt.show()