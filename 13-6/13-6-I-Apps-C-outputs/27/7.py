
def get_max_spies(n, pattern):
    # Calculate the number of 1s in the pattern
    num_ones = pattern.count('1')
    
    # Calculate the number of stars in the pattern
    num_stars = pattern.count('*')
    
    # If the number of 1s is equal to the number of stars,
    # then the pattern is valid for all binary strings of length n
    if num_ones == num_stars:
        return 2**n
    
    # If the number of 1s is less than the number of stars,
    # then the pattern is valid for some binary strings of length n
    else:
        # Calculate the number of possible substrings that satisfy the pattern
        num_substrings = (2**(n-num_ones)) * (num_ones + num_stars)
        return num_substrings

