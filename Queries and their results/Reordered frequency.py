# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:22:15 2018

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
grouped = order_products_all.groupby("reordered")["product_id"].aggregate({'Total_products': 'count'}).reset_index()
grouped['Ratios'] = grouped["Total_products"].apply(lambda x: x /grouped['Total_products'].sum())
grouped
grouped  = grouped.groupby(['reordered']).sum()['Total_products'].sort_values(ascending=False)

sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(5, 8))
sns.barplot(grouped.index, grouped.values, palette='RdBu_r')
plt.ylabel('Number of Products', fontsize=13)
plt.xlabel('Reordered or Not Reordered', fontsize=13)
plt.ticklabel_format(style='plain', axis='y')
plt.show()