def add_elements(arr, k):
    
    sum_ = 0
    for i in range(k):
        if arr[i] < 10:
            sum_ += arr[i]
        elif arr[i] < 100:
            sum_ += arr[i]
        else:
            sum_ += arr[i] // 10
    return sum_


if