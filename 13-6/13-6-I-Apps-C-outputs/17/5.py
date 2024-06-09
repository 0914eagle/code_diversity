
def get_smallest_t(n, crushes):
    # Initialize a dictionary to store the number of rounds needed for each person to become the Joon-Joon
    rounds = {i: 0 for i in range(1, n + 1)}
    
    # Loop through each person and their crush
    for i in range(1, n + 1):
        crush = crushes[i - 1]
        if crush == i:
            # If the person is their own crush, they become the Joon-Joon immediately
            rounds[i] = 1
        else:
            # If the person is not their own crush, they need to call their crush and wait for them to call them back
            rounds[i] = rounds[crush] + 1
    
    # Find the smallest value of t that satisfies the condition for all people
    smallest_t = float('inf')
    for i in range(1, n + 1):
        if rounds[i] < smallest_t:
            smallest_t = rounds[i]
    
    # If there is no t that satisfies the condition, return -1
    if smallest_t == float('inf'):
        return -1
    
    # Otherwise, return the smallest t
    return smallest_t

