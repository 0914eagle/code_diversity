def add_elements(arr, k):
    
    if not arr:
        return 0
    if k == 1:
        return arr[0]
    if k == 2:
        return arr[0] + arr[1]
    if k == 3:
        return arr[0] + arr[1] + arr[2]
    if k == 4:
        return arr[0] + arr[1] + arr[2] + arr[3]
    if k == 5:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
    if k == 6:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5]
    if k == 7:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6]
    if k == 8:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7]
    if k == 9:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8]
    return 0


