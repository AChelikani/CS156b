import pandas as pd 
SVD40 = pd.read_table('SVD1.dta', delim_whitespace = True, header = None)
SVD65 = pd.read_table('SVD2.dta', delim_whitespace = True, header = None)
SVD70 = pd.read_table('SVD3.dta', delim_whitespace = True, header = None)
combined = pd.concat([SVD40, SVD65, SVD70])
average = combined.mean(axis = 1)
average.to_csv('avg1.csv', index=False)