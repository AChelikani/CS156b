from surprise import SVD, BaselineOnly, Reader, evaluate, Dataset
import os
from pprint import pprint
import pandas
import time

start_time = time.time()


df = pandas.read_csv("um/separated/base_training_data.dta", delimiter=' ', header=None)
#data = Dataset.load_from_file("um/separated/base_training_data_tabbed.dta", reader=reader)
df.columns = ['user', 'item', 'timestamp', 'rating']
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)
del df
print "Dataset loaded...\n"

trainset = data.build_full_trainset()
del data
print "Trainset built...\n"

algo = SVD(verbose=True, n_factors=100, n_epochs=1, lr_all=0.005)

algo.fit(trainset)
print "Algorithm fitted...\n"
print("--- %s seconds ---\n" % (time.time() - start_time))
start_time_prediction = time.time()

qual_df = pandas.read_csv("um/separated/qual_test_data.dta", delim_whitespace=True, names=["User", "Movie", "Date"])
output_file = open("um/output/svd_surprise.dta", "w")

print "Qual data loaded...\n"
row_counter = 0

for row in qual_df.itertuples(index=True, name="Qual Data"):
    user, movie, date, rating = row
    pred = algo.predict(uid=user, iid=movie)
    row_counter += 1
    if (row_counter%10000==0):
        print row_counter
    output_file.write(str(pred[3]) + "\n")

output_file.close()
print("--- %s seconds ---\n" % (time.time() - start_time_prediction))
