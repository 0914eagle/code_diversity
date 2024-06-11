def pairs_sum_to_zero(l):
    
    # Your code here
    # set() is a built-in function that returns a set of unique values
    # set(l) returns a set of unique values in l
    # set(l) - {0} returns a set of unique values in l, except for 0
    # len(set(l) - {0}) returns the number of unique values in l, except for 0
    # if len(set(l) - {0}) > 1, then there are at least two distinct elements
    # in l that sum to zero
    return len(set(l) - {0}) > 1


