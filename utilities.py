import pandas

def generate_positions_from_index(idx_file_value, idx_file_path, output_file_path=None):
    df = pandas.read_csv(idx_file_path, delim_whitespace=True, names=["Index"])
    print "Lines Analyzed: " + str(len(df)) + " from " + idx_file_path
    df = df[df["Index"] == idx_file_value]
    df = df.drop("Index", 1)
    if (output_file_path):
        df.to_csv(output_file_path, sep=" ", header=False, index=True)
        print "Lines Written: " + str(len(df)) + " to " + output_file_path
    return df.index.tolist()

def create_partitioned_data_file(idx_file_value, idx_file_path, data_file_path, output_file_path):
    all_df = pandas.read_csv(data_file_path, delim_whitespace=True, names=["User", "Movie", "Date", "Rating"])
    print "Lines Analyzed: " + str(len(all_df)) + " from " + data_file_path
    indices = generate_positions_from_index(idx_file_value, idx_file_path)
    df = all_df[all_df.index.isin(indices)]
    df.drop(columns=["Date"])
    df.to_csv(output_file_path, sep="\t", header=False, index=False)
    print "Lines Written: " + str(len(df)) + " to " + output_file_path

def generate_averages(base_data_file_path):
    df = pandas.read_csv(base_data_file_path, delim_whitespace=True, names=["User", "Movie", "Date", "Rating"])
    print "Lines Analyzed: " + str(len(df)) + " from " + str(base_data_file_path)
    user_means = df.groupby(["User"])["Rating"].mean()
    movie_means = df.groupby(["Movie"])["Rating"].mean()
    user_means.to_csv("generated/user_averages.dta", sep=" ", header=False, index=True)
    print "Lines Written: " + str(len(user_means)) + " to generated/user_averages.dta"
    movie_means.to_csv("generated/movie_averages.dta", sep=" ", header=False, index=True)
    print "Lines Written: " + str(len(movie_means)) + " to generated/movie_averages.dta"




if __name__ == "__main__":
    #create_partitioned_data_file(5, "um/all.idx", "um/all.dta", "um/separated/qual_test_data.dta")
    #create_partitioned_data_file(1, "mu/all.idx", "mu/all.dta", "mu/separated/base_training_data.dta")
    #generate_averages("um/separated/base_training_data.dta")
    create_partitioned_data_file(2, "um/all.idx", "um/all.dta", "um/separated/subset_base_training_data.dta")
