# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 02:30:32 2018

@author: JIM
"""

import sys
import pandas as pd

#%% CSV Splitter

# THIS NEEDS TO BE CHANGED ACCORDING TO USER
data_path = '../../um/all.dta'

print('now reading all.dta')
df = pd.read_csv(data_path, delimiter=' ', header=None)
print('size:', sys.getsizeof(df))
df.columns = ['user', 'movie', 'date', 'rating']

print('splitting data into train and test...')
to_predict = df[df.rating==0]
usable = df[df.rating!=0]
del df

print('now saving test set')
to_predict.to_csv('../custom_data/test.csv', index=False, header=False, sep=' ')
print('now saving train set')
usable.to_csv('../custom_data/training.csv', index=False, header=False, sep=' ')
print('done')