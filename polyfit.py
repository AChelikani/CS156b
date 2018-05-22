import numpy as np
import time

def predictUserRating(user_train, user_qual, ratings, d):
    train = np.array(user_train)
    qual  = np.array(user_qual)
    if len(qual) > 0:
        if len(train) == 0:                   # Shouldn"t ever happen
            for r in qual:
                ratings.append(r)
        elif len(train) < 5:                  # Arbitrary N <= d + 1
            p = np.mean(train[:,0])
            for r in qual:
                ratings.append(0.5*p + 0.5*r) # Average of average
        else:
            p = np.polyfit(train[:,1], train[:,0], d) # Polyfit
            for r in qual:
                ratings.append(np.polyval(p, r))

mu_path = "../mu/"
um_path = "../um/"

# Compute movie averages
print(time.asctime(), "computing movie averages")
n_tot = 102416306
n_train = 99666408
n_qual = 2749898
n_mov = 17770
n_user = 458293
n_days = 2243

mov_mean = np.zeros(n_mov + 1, dtype=float)
mov_counts = np.zeros(n_mov + 1, dtype=float)
with open(mu_path + "all.dta") as f:
    for line in f:
        l = map(int, line.split())
        mov_mean[l[1]] += l[3]
        mov_counts[l[1]] += float(l[3] != 0)
mov_counts[0] = 1
mov_mean = np.divide(mov_mean, mov_counts)

# Polynomial regression for each user (degree d)
# (y,x) = (their rating, mean reating)
print(time.asctime(), "computing polyfit prediction")
d = 3
user = 1
user_train = []
user_qual = []
user_user = []
ratings = []
count_train = 0
count_qual = 0
with open(um_path + "all.dta") as f:
    for line in f:
        l = map(int, line.split())
        if l[0] != user:
            predictUserRating(user_train, user_qual, ratings, d)
            
            # Go to next user
            user = l[0]
            user_train = []
            user_qual = []
        
        if l[3] == 0:
            user_qual.append(mov_mean[l[1]])
            count_qual += 1
        else:
            user_train.append([l[3], mov_mean[l[1]]])
            count_train += 1

# Add last user"s quals
predictUserRating(user_train, user_qual, ratings, d)

#ratings_rounded = np.round(ratings)
print(time.asctime(), "writing output")
output = open("polyfit_rating.dta", "w")
lines_added = 0
for r in ratings:
    r_round = r
    if r_round < 1:
        r_round = 1
    elif r_round > 5:
        r_round = 5
    output.write(str(r_round) + "\n")
    lines_added += 1
output.close()
print "Lines added: " + str(lines_added)