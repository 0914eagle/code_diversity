
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
    
    # Initialize a dictionary to store the number of good arrays for each suffix sum
    suffix_sum_count = {}
    suffix_sum_count[0] = 1
    
    # Iterate through the array in reverse and calculate the suffix sum
    suffix_sum = 0
    for i in range(n-1, -1, -1):
        suffix_sum += a[i]
        if suffix_sum in suffix_sum_count:
            suffix_sum_count[suffix_sum] += 1
        else:
            suffix_sum_count[suffix_sum] = 1
    
    # Initialize the number of good arrays to 0
    good_arrays = 0
    
    # Iterate through the prefix sum dictionary and calculate the number of good arrays
    for prefix_sum, count in prefix_sum_count.items():
        if prefix_sum in suffix_sum_count:
            good_arrays += count * suffix_sum_count[prefix_sum]
    
    # Return the number of good arrays modulo 998244353
    return good_arrays % 998244353

