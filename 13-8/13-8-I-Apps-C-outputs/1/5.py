
def solve(m, k, a, b):
    # Calculate the total number of sweets Danny has eaten
    total_sweets = sum(b)
    
    # Calculate the maximum number of additional sweets that Danny can buy
    max_sweets = m - total_sweets
    
    # If the maximum number of additional sweets is greater than or equal to k, then Danny can buy k additional sweets and keep his diet balanced
    if max_sweets >= k:
        return k
    
    # If the maximum number of additional sweets is less than k, then Danny can buy all the additional sweets and still keep his diet balanced
    else:
        return max_sweets

