# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:30:29 2018

@author: Koushik
"""

import pandas as pd
from IPython.display import display
import sys
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 19:04:35 2018

@author: Koushik
"""

#Python 2.x program for Speech Recognition
 
import re
#enter the name of usb microphone that you found
#using lsusb
#the following name is only used as an example
#mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
#device_id = "MMDEVAPI\AudioEndpoints"
#Sample rate is how often values are recorded
#mic_list = sr.Microphone.list_microphone_names()
 
#the following loop aims to set the device ID of the mic that
#we specifically want to use to avoid ambiguity.
#for i, microphone_name in enumerate(mic_list):
 #   if microphone_name == mic_name:
  #      device_id = i
 
#use the microphone as source for input. Here, we also specify 
#which device ID to specifically look for incase the microphone 
#is not working, an error will pop up saying "device_id undefined"
products  = pd.read_csv('products.csv')
products = products['product_name'].tolist();
for i in range(0,len(products)):
    products[i] = products[i].lower()
#print(products)
text = ' '.join(sys.argv[1:])
text = re.split(' and |order |some | like | love |',text)
#print(text)
new_text = ''
for i in text:
    print(i)
    if i in products:
        new_text+=i+","
new_text = new_text.split(',')
#print(new_text)
analysis = pd.read_csv("output.csv")
analysis["itemA"]=analysis['itemA'].str.lower()

#item_name = ("The Red ONe: Squished Fruit Smoothies","Santa Fe Extra Lean Veggie Burger")
#print(analysis['itemA'])
#columns = ["itemB"]
#df[df['B']==3]['A']
analysis_specific_data = pd.DataFrame()
for i in new_text:
    analysis_specific = analysis.loc[analysis['itemA']==i]
    analysis_specific_data = analysis_specific_data.append(analysis_specific)
#print(analysis_specific)

analysis_specific_data = analysis_specific_data.sort_values('lift',ascending = False)
analysis_specific_data.to_html('recommend_table.html')
