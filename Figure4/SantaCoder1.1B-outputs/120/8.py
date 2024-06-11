def maximum(arr, k):
    
    if not arr:
        return []
    if k == 1:
        return arr
    if k == 2:
        return sorted(arr, reverse=True)
    if k == 3:
        return sorted(arr)
    if k == 4:
        return sorted(arr, key=lambda x: x[0] * x[1])
    if k == 5:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2])
    if k == 6:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3])
    if k == 7:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3] * x[4])
    if k == 8:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3] * x[4] * x[5])
    if k == 9:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3] * x[4] * x[5] * x[6])
    if k == 10:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3] * x[4] * x[5] * x[6] * x[7])
    if k == 11:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3] * x[4] * x[5] * x[6] * x[7] * x[8])
    if k == 12:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3] * x[4] * x[5] * x[6] * x[7] * x[8] * x[9])
    if k == 13:
        return sorted(arr, key=lambda x: x[0] * x[1] * x[2] * x[3]