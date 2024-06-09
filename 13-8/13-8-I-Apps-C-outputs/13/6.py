
def solve(n, k, a):
    # Initialize a set to store the possible values of d
    possible_d = set()
    
    # Iterate over each denomination of banknote
    for i in range(n):
        # Calculate the value of the banknote in the Martian number system
        value = int(str(a[i])[::-1])
        
        # If the value ends with the digit d, add it to the set of possible values
        if str(value)[-1] == str(d):
            possible_d.add(value)
    
    # Return the number of possible values of d and the set of possible values
    return len(possible_d), possible_d

