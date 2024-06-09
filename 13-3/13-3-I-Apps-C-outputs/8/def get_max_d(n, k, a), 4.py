
def get_max_d(n, k, a):
    # Initialize variables
    d = 0
    total_length = 0
    
    # Loop through each bamboo and check if it has reached the required height
    for i in range(n):
        # If the bamboo has reached the required height, add its length to the total length
        if a[i] <= d:
            total_length += d - a[i] + 1
    
    # If the total length is less than or equal to k, return d
    if total_length <= k:
        return d
    
    # If the total length is greater than k, increase d by 1 and repeat the process
    else:
        d += 1
        return get_max_d(n, k, a)

