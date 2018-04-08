# Stats
# RMSE = 1.06626
# % Above Water = -12.0727%

user_to_rating_sum = {}
user_to_num_rated = {}
user_to_avg_rating = {}

with open("um/seperated/base_training_data.dta") as f:
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

    for user in user_to_rating_sum:
        user_to_avg_rating[user] = float(user_to_rating_sum[user])/float(user_to_num_rated[user])

    output = open("um/output/avg_user_rating.dta", "w")
    qual_data = open("um/seperated/qual_test_data.dta", "r")
    lines_added = 0
    for line in qual_data:
        user, movie, date, rating = map(int, line.rstrip().split())
        output.write(str(user_to_avg_rating[user]) + "\n")
        lines_added += 1

    output.close()
    qual_data.close()
    print "Lines added: " + str(lines_added)
