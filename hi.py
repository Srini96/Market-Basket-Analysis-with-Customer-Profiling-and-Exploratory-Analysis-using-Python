#!C:/Python3.6/python.exe
import cgi
import sys
import pandas as pd
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 19:04:35 2018

@author: Koushik
"""

#Python 2.x program for Speech Recognition
 
#import re
print("content-type: text/html\n\n" )
#print("<br><B>hello python yo</B>")
#var = self.request.get('q')
form = cgi.FieldStorage()
text = form.getvalue('q')
#products  = pd.read_csv('products.csv')
#products = products['product_name'].tolist();
#for i in range(0,len(products)):
 #   products[i] = products[i].lower()
#print(products)
#text = re.split(' and |order |some | like | love |',text)
#print(text)
#new_text = ''
#for i in text:
    #print(i)
#    if i in products:
 #       new_text+=i+","
#new_text = new_text.split(',')
#print(new_text)
#analysis = pd.read_csv("output.csv")
#analysis["itemA"]=analysis['itemA'].str.lower()

#item_name = ("The Red ONe: Squished Fruit Smoothies","Santa Fe Extra Lean Veggie Burger")
#print(analysis['itemA'])
#columns = ["itemB"]
#df[df['B']==3]['A']
#analysis_specific_data = pd.DataFrame()
#for i in new_text:
#    analysis_specific = analysis.loc[analysis['itemA']==i]
 #   analysis_specific_data = analysis_specific_data.append(analysis_specific)
#print(analysis_specific)

#analysis_specific_data = analysis_specific_data.sort_values('lift',ascending = False)
#analysis_specific_data.to_html('recommend_table.html')
#f = open('recommend_table.html','r')
#print(f.read())