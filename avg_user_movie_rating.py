# Stats
# With user_coef = .5 and movie_coef = 0.5
# RMSE: 1.01439
# % Above Water = -6.6208%

user_to_rating_sum = {}
user_to_num_rated = {}
user_to_avg_rating = {}

movie_to_rating_sum = {}
movie_to_num_rated = {}
movie_to_avg_rating = {}


with open("um/separated/base_training_data.dta") as f:
    for line in f:
        user, movie, date, rating = map(int, line.rstrip().split())
        if user not in user_to_rating_sum:
            user_to_rating_sum[user] = rating
        else:
            user_to_rating_sum[user] += rating

        if user not in user_to_num_rated:
            user_to_num_rated[user] = 1
        else:
            user_to_num_rated[user] += 1

        if movie not in movie_to_rating_sum:
            movie_to_rating_sum[movie] = rating
        else:
            movie_to_rating_sum[movie] += rating

        if movie not in movie_to_num_rated:
            movie_to_num_rated[movie] = 1
        else:
            movie_to_num_rated[movie] += 1

    for user in user_to_rating_sum:
        user_to_avg_rating[user] = float(user_to_rating_sum[user])/float(user_to_num_rated[user])

    for movie in movie_to_rating_sum:
        movie_to_avg_rating[movie] = float(movie_to_rating_sum[movie])/float(movie_to_num_rated[movie])

print "Constructed user and movie averages...\n"




output = open("um/output/avg_user_movie_rating.dta", "w")
qual_data = open("um/separated/qual_test_data.dta", "r")
user_coefficient = 0.5
movie_coefficient = 0.5
lines_added = 0
assert(user_coefficient + movie_coefficient == 1.0)
for line in qual_data:
    user, movie, date, rating = map(int, line.rstrip().split())
    avg_user_rating = user_to_avg_rating[user]
    avg_movie_rating = movie_to_avg_rating[movie]
    final_rating = user_coefficient * avg_user_rating + movie_coefficient * avg_movie_rating
    output.write(str(final_rating) + "\n")
    lines_added += 1

output.close()
qual_data.close()
print "Lines added: " + str(lines_added)
