from surprise import SVD, BaselineOnly, Reader, evaluate, Dataset
import os
from surprise.model_selection import cross_validate

file_path = os.path.expanduser('um/separated/probe_training_data.dta')

reader = Reader(line_format='user item timestamp rating', sep='\t')

data = Dataset.load_from_file("um/separated/probe_training_data.dta", reader=reader)

data.split(n_folds=5)
algo = SVD()

cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

trainset = data.build_full_trainset()
algo.train(trainset)

'''
f = open("um/separated/qual_test_data.dta", "r")
for line in f:
    user, movie, timestamp = map(int, line.rstrip().split(" "))
'''

userid = 1
itemid = 3912
pred = algo.predict(uid=userid, iid=itemid, verbose=2)
f = open("um/output/")
print pred
