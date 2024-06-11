def add_elements(arr, k):
    
    # Your code here
    sum = 0
    for i in range(k):
        if arr[i] < 100:
            sum += arr[i]
    return sum


