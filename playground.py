import utilities

if __name__ == "__main__":
    '''
    with open("um/seperated/qual_test_data.dta", "r") as f:
        for line in f:
            print line
            break
    '''
    num_lines = 0
    with open("um/example.dta") as f:
        for line in f:
            num_lines += 1
    print "Lines in output test file: " + str(num_lines)
    
