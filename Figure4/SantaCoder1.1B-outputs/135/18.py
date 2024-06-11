def can_arrange(arr):
    
    if len(arr) < 2:
        return -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            return i
    return -1

if __name__ == '__main__':
    arr = [1,2,4,3,5]
    print(can_arrange(arr))