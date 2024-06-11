def sort_array(arr):
    
    arr.sort(key=lambda x: x // 10)
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
    return arr


