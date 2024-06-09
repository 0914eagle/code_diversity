
def f1(n, a, b, c):
    # Convert the input lists to sets for O(1) lookup
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    
    # Initialize a counter for the number of pairs
    count = 0
    
    # Iterate over each camel in a_set
    for camel in a_set:
        # If the camel is also in b_set and c_set, increment the counter
        if camel in b_set and camel in c_set:
            count += 1
    
    return count

