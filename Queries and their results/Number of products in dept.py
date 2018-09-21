# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:22:11 2018

@author: KURAMS
"""

import pandas as pd

import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
color = sns.color_palette()

import warnings
warnings.filterwarnings('ignore')
aisles_df= pd.read_csv("./input/aisles.csv")
departments_df= pd.read_csv("./input/departments.csv")
order_products_prior_df= pd.read_csv("./input/order_products_prior.csv")
order_products_train_df= pd.read_csv("./input/order_products_train.csv")
orders_df= pd.read_csv("./input/orders.csv")
products_df= pd.read_csv("./input/products.csv")

order_products_all = pd.concat([order_products_train_df, order_products_prior_df], axis=0)
items  = pd.merge(left =pd.merge(left=products_df, right=departments_df, how='left'), right=aisles_df, how='left')
items.head()
grouped = items.groupby("aisle")["product_id"].aggregate({'Total_products': 'count'}).reset_index()
grouped['Ratio'] = grouped["Total_products"].apply(lambda x: x /grouped['Total_products'].sum())
grouped = grouped.sort_values(by='Total_products', ascending=False)[:20]
grouped

grouped  = grouped.groupby(['aisle']).sum()['Total_products'].sort_values(ascending=False)

f, ax = plt.subplots(figsize=(12, 15))
plt.xticks(rotation='vertical')
sns.barplot(grouped.index, grouped.values)
plt.ylabel('Number of products', fontsize=13)
plt.xlabel('Aisles', fontsize=13)
plt.show()

