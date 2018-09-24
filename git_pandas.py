# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:45:16 2018

@author: jrgan
"""

#%%

#Check if the related packages are ok (do not get an error)
#ModuleNotFoundError: No module named 'pandas'
import pandas as pd
import numpy as np

#%%

my_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'age': [42, 52, 36, 24, 73], 
        'RFM_Star': [5, 1, 3, None,2],
        'AvgSpend': [100, 2.5,57,62, 45]}

df = pd.DataFrame(my_data,
                  index=['C1','C2','C3','C4','C5'],
                  columns = ['first_name','age', 'RFM_Star', 'AvgSpend'])

#Exercise uncomment the next lines and check the average of all
df.mean(0)
df["age"].mean()


#Get the mean of the Average Spending
