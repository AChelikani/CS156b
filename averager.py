# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 02:30:32 2018

@author: JIM
"""

import sys
import pandas as pd
import numpy as np

#%% Sorter

data_path = 'data/subset-user.txt'
data_path = '../../um/all.dta'

df = pd.read_csv(data_path, delimiter=' ', header=None)
print(sys.getsizeof(df))
df.columns = ['user', 'movie', 'date', 'rating']

to_predict = df[df.rating==0]
usable = df[df.rating!=0]
del df

#%% Calculator

to_predict = to_predict.values.T[0:2].T
predicted = np.zeros(len(to_predict))
user_means = np.zeros(np.max(usable.user))
movie_means = np.zeros(np.max(usable.movie))
for i in range(len(to_predict)):
    want_user = to_predict[i][0]
    want_movie = to_predict[i][1]
    
    if user_means[want_user-1] != 0:
        usermean = user_means[want_user-1]
    else:
        user_means[want_user-1] = np.mean(usable[usable.user==want_user].rating)
        usermean = user_means[want_user-1]
    
    if movie_means[want_movie-1] != 0:
        moviemean = movie_means[want_movie-1]
    else:
        movie_means[want_movie-1] = np.mean(usable[usable.movie==want_movie].rating)
        moviemean = movie_means[want_movie-1]
    
    predicted[i] = (usermean + moviemean) / 2
    if i % 1000 == 0:
        print(i, 'of', len(to_predict))

np.savetxt('results.dta', predicted, fmt='%.3f')