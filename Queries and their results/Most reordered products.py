# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:22:59 2018

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

products_df= pd.read_csv("./input/products.csv")
order_products_all = pd.concat([order_products_train_df, order_products_prior_df], axis=0)

grouped = order_products_all.groupby("product_id")["reordered"].aggregate({'reorder_sum': sum,'reorder_total': 'count'}).reset_index()
grouped['reorder_probability'] = grouped['reorder_sum'] / grouped['reorder_total']
grouped = pd.merge(grouped, products_df[['product_id', 'product_name']], how='left', on=['product_id'])
grouped = grouped[grouped.reorder_total > 75].sort_values(['reorder_probability'], ascending=False)[:10]
grouped

print(grouped)

grouped  = grouped.groupby(['product_name']).sum()['reorder_probability'].sort_values(ascending=False)

sns.set_style('darkgrid')
f, ax = plt.subplots(figsize=(12, 10))
plt.xticks(rotation='vertical')
sns.barplot(grouped.index, grouped.values)
plt.ylim([0.85,0.95])
plt.ylabel('Reorder probability', fontsize=13)
plt.xlabel('Most reordered products', fontsize=12)
plt.show()