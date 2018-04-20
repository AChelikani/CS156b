from surprise import SlopeOne, BaselineOnly, Reader, evaluate, Dataset
import os
from surprise.model_selection import cross_validate

file_path = os.path.expanduser('um/separated/probe_training_data.dta')

reader = Reader(line_format='user item timestamp rating', sep='\t')

data = Dataset.load_from_file("um/separated/probe_training_data.dta", reader=reader)

algo = SlopeOne()

trainset = data.build_full_trainset()
algo.train(trainset)

#userid = 1
#itemid = 3912

output = open("um/output/slopeone.dta", "w")
for u in range(1, 458294):
    for i in range(1, 17771):
        pred = algo.predict(uid = u, iid = i, verbose = 2)
        output.write(str(pred)+"\n")
output.close()

