def add_elements(arr, k):
    
    result = 0
    for i in range(k):
        if arr[i] < 10:
            result += arr[i]
        elif arr[i] < 100:
            result += arr[i]
        else:
            result += arr[i] // 10
    return result


if