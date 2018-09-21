# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:44:26 2018

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
items = pd.merge(left=pd.merge(left=products_df, right=departments_df, how='left'), right=aisles_df, how='left')
items.head()

users_flow = orders_df[['user_id', 'order_id']].merge(order_products_train_df[['order_id', 'product_id']],
                                          how='inner', left_on='order_id', right_on='order_id')

users_flow = users_flow.merge(items, how='inner', left_on='product_id',
                                         right_on='product_id')

grouped = users_flow.groupby("department")["order_id"].aggregate({'Total_orders': 'count'}).reset_index()
grouped['Ratio'] = grouped["Total_orders"].apply(lambda x: x /grouped['Total_orders'].sum())
grouped.sort_values(by='Total_orders', ascending=False, inplace=True)
grouped

print(grouped)
grouped  = grouped.groupby(['department']).sum()['Total_orders'].sort_values(ascending=False)

f, ax = plt.subplots(figsize=(12, 15))
plt.xticks(rotation='vertical')
sns.barplot(grouped.index, grouped.values)
plt.ylabel('Number of Orders', fontsize=13)
plt.xlabel('Departments', fontsize=13)
plt.show()