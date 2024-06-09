
def solve(r, b, k):
    # Calculate the maximum number of consecutive planks with the same color
    max_consecutive = k
    
    # Check if r and b are both factors of max_consecutive
    if r % max_consecutive == 0 and b % max_consecutive == 0:
        return "OBEY"
    else:
        return "REBEL"

