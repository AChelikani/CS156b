# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:20:51 2018

@author: PITAHAYA
"""

import numpy as np

def create_matrix(n, m):
    result = np.zeros((n,m))
    with open("um/all.dta") as lines:
        for line in lines:
            user = int(line.split(' ')[0])
            movie = int(line.split(' ')[1])
            rating = int(line.split(' ')[3][0])
            if (rating != 0):
                result[user-1][movie-1] = rating
                if not (user%10000):
                    print(user, movie, rating)
            else:
                result[user-1][movie-1] = np.nan
    return result

def find_mean(array, row, col):
    row_mean = np.nanmean(array[row-1])
    col_mean = np.nanmean(array.T[col-1])
    return (row_mean + col_mean) / 2

um_matrix = create_matrix(458293, 17770)
print(find_mean(um_matrix, 5, 5))