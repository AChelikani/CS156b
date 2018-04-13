from surprise import SVD
from surprise import BaselineOnly
from surprise import Reader

import os
from surprise.model_selection import cross_validate

file_path = os.path.expanduser('um/separated/probe_training_data.dta')

reader = Reader(line_format='user item timestamp rating', sep='\s')

data = Dataset.load_from_file(file_path, reader=reader)

# We can now use this dataset as we please, e.g. calling cross_validate
cross_validate(BaselineOnly(), data, verbose=True)
