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


if __name__ == '__main__':
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([1, 2, 3]) == [2, 1]
    assert pluck([]) == []
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,