def pluck(arr):
    
    if not arr:
        return []
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] % 2 == 0 else arr[1]
    if len(arr) == 3:
        return arr[0] if arr[0] % 2 == 0 else arr[1] if arr[1] % 2 == 0 else arr[2]
    if len(arr) == 4:
        return arr[0] if arr[0] % 2 == 0 else arr[1] if arr[1] % 2 == 0 else arr[2] if arr[2] % 2 == 0 else arr[3]
    if len(arr) == 5:
        return arr[0] if arr[0] % 2 == 0 else arr[1] if arr[1] % 2 == 0 else arr[2] if arr[2] % 2 == 0 else arr[3] if arr[3] % 2 == 0 else arr[4]
    return []


