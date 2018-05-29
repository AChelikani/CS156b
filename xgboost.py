import xgboost as xgboostfrom
from xgboost import XGBClassifier
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import os
import numpy as np
import pandas as pd
from surprise.model_selection import cross_validate
import time

file_path = '../custom_data/training.csv'
reader = Reader(line_format='user item timestamp rating', sep='\t')
print(time.asctime(), 'loading training data')
df = pd.read_csv(file_path, delimiter=' ', header=None)
df.columns = ['user', 'item', 'timestamp', 'rating']
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)
del df
print(time.asctime(), 'loaded training data, now building trainset')
trainset = data.build_full_trainset()
del data

title = 'XGB'
algo = XGBClassifier()
algo.fit(trainset)

print(time.asctime(), 'training complete, now loading prediction data')
to_predict = pd.read_csv(file_path_test, delimiter=' ', header=None)
to_predict = to_predict.values.T[0:2].T
predicted = np.zeros(len(to_predict))

print(time.asctime(), 'prediction data loaded, now predicting')
for i in range(len(predicted)):
    user = to_predict[i][0]
    item = to_predict[i][1]
    predicted[i] = algo.predict(uid=user, iid=item, verbose=0).est
    if (i%500000 == 0):
        print(i, 'of', len(predicted), 'predicted')

print(time.asctime(), 'saving predictions')

np.savetxt('../custom_data/'+title+'.dta', predicted, fmt='%.3f')

print(time.asctime(), 'done')
