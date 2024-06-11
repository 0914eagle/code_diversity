def maximum(arr, k):
    
    if not arr:
        return []
    if k == 1:
        return arr
    if k == 2:
        return max(arr)
    if k == 3:
        return max(arr, key=lambda x: x[0])
    if k == 4:
        return max(arr, key=lambda x: x[1])
    if k == 5:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1])
    if k == 6:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 7:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 8:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 9:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 10:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 11:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 12:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 13:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 14:
        return max(arr, key=lambda x: x[0] if x[1] > x[0] else x[1], reverse=True)
    if k == 15:
        return max(arr, key=lambda x: x[0] if x[