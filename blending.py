import pandas
from sklearn.linear_model import LinearRegression

# Read in probe data file and all solutions to blend together
# All solutions need to be predictions of probe data set

probe_set = pandas.read_csv("um/separated/probe_training_data.dta", delim_whitespace=True, names=["User", "Movie", "Date", "Rating"])
probe_set.drop(columns=["User, Movie, Date"])

#   T0 T1 T2 ...
# [              ]        [coef1]         [probe_set_1]
# [              ]    *   [coef2]    =    [probe_set_2]
# [              ]        [coef3]         [probe_set_3]
# ................        ......          ............
#
# Coefs = (T^T*T)^-1 * (T)^T * probe
# Estimate with linear regression

# Read in all solutions (predictions on probe) into one pandas df
# df = ...

regression_model = LinearRegression()
regression_model.fit(df, probe_set)

for idx, col_name in enumerate(df.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

intercept = regression_model.intercept_[0]

print("The intercept for our model is {}".format(intercept))
