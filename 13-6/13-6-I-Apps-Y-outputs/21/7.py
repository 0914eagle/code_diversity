
def get_maximum_sum_of_absolute_differences(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Fill the array in a way that the sum of elements is m
    for i in range(n):
        arr[i] = m // n
        m -= m // n
    
    # Calculate the sum of absolute differences between adjacent elements
    sum_abs_diff = 0
    for i in range(n - 1):
        sum_abs_diff += abs(arr[i] - arr[i + 1])
    
    return sum_abs_diff

