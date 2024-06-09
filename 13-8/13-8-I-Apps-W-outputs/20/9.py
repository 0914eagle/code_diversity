
def get_magical_permutation(n, s):
    # Initialize a set to store the elements of S
    set_s = set(s)
    # Initialize a list to store the magical permutation
    permutation = []
    # Initialize a variable to store the largest non-negative integer x
    x = 0
    # Loop through all possible values of x
    for x in range(n):
        # Loop through all possible values of the permutation
        for i in range(2**x):
            # Check if the bitwise xor of any two consecutive elements in the permutation is an element in S
            if i ^ (i+1) in set_s:
                # Add the permutation to the list
                permutation.append(i)
                break
        # If the list is complete, break the loop
        if len(permutation) == 2**x:
            break
    # Return the largest non-negative integer x and the magical permutation
    return x, permutation

