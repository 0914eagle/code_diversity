def add_elements(arr, k):
    
    if k == 0:
        return 0

    # find the largest number with at most 2 digits
    # and sum up all numbers smaller than it
    max_num = 0
    for i in range(k):
        max_num = max(max_num, arr[i])

    return sum(num for num in arr[:k] if num <= max_num)
