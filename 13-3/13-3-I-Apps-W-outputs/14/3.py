
def count_good_arrays(n, k, a):
    # Initialize a dictionary to store the number of good arrays for each prefix sum
    prefix_sum_count = {}
    prefix_sum_count[0] = 1
    
    # Iterate through the array and calculate the prefix sum
    prefix_sum = 0
    for i in range(n):
        prefix_sum += a[i]
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1
        else:
            prefix_sum_count[prefix_sum] = 1
    
    # Initialize a dictionary to store the number of bad arrays for each prefix sum
    prefix_sum_bad_count = {}
    prefix_sum_bad_count[0] = 0
    
    # Iterate through the array and calculate the prefix sum
    prefix_sum = 0
    for i in range(n):
        prefix_sum += a[i]
        if prefix_sum in prefix_sum_bad_count:
            prefix_sum_bad_count[prefix_sum] += 1
        else:
            prefix_sum_bad_count[prefix_sum] = 1
    
    # Initialize the answer
    answer = 0
    
    # Iterate through the prefix sums and calculate the number of good arrays
    for prefix_sum in prefix_sum_count:
        answer += prefix_sum_count[prefix_sum] * prefix_sum_bad_count[prefix_sum]
    
    # Return the answer modulo 998244353
    return answer % 998244353

