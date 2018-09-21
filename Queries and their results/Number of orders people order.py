
import pandas as pd

import matplotlib.pyplot as plt 
import seaborn as sns
color = sns.color_palette()



aisles_df= pd.read_csv("./input/aisles.csv")
departments_df= pd.read_csv("./input/departments.csv")
order_products_prior_df= pd.read_csv("./input/order_products_prior.csv")
order_products_train_df= pd.read_csv("./input/order_products_train.csv")
orders_df= pd.read_csv("./input/orders.csv")
products_df= pd.read_csv("./input/products.csv")

order_products_all = pd.concat([order_products_train_df, order_products_prior_df], axis=0)

grouped = order_products_all.groupby("order_id")["add_to_cart_order"].aggregate("max").reset_index()
grouped = grouped.add_to_cart_order.value_counts()

sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(10, 12))
plt.xticks(rotation='vertical')
sns.barplot(grouped.index, grouped.values)

plt.ylabel('Number of Orders', fontsize=17)
plt.xlabel('Number of products added in order', fontsize=15)
plt.show()