# Stats
# With user_coef = .5 and movie_coef = 0.5
# RMSE: 1.01439
# % Above Water = -6.6208%
import pandas

user_to_rating_sum = {}
user_to_num_rated = {}
user_to_avg_rating = {}

movie_to_rating_sum = {}
movie_to_num_rated = {}
movie_to_avg_rating = {}


users_df = pandas.read_csv("generated/user_averages.dta", delim_whitespace=True, names=["User", "Rating"])
movies_df = pandas.read_csv("generated/movie_averages.dta", delim_whitespace=True, names=["Movie", "Rating"])

print "Constructed user and movie averages...\n"

#probe_data = open("um/separated/probe_training_data.dta", "r")

output = open("um/output/avg_user_40_movie_60_rating.dta", "w")
qual_data = open("um/separated/qual_test_data.dta", "r")
user_coefficient = 0.4
movie_coefficient = 0.6
lines_added = 0
assert(user_coefficient + movie_coefficient == 1.0)
for line in qual_data:
    user, movie, date, rating = map(int, line.rstrip().split())
    avg_user_rating = users_df.at[user-1, "Rating"]
    avg_movie_rating = movies_df.at[movie-1, "Rating"]
    final_rating = user_coefficient * avg_user_rating + movie_coefficient * avg_movie_rating
    output.write(str(final_rating) + "\n")
    lines_added += 1

output.close()
qual_data.close()
print "Lines added: " + str(lines_added)
