def sort_array(arr):
    
    # Your code here
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
    return arr


