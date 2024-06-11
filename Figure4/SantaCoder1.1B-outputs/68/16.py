def pluck(arr):
    
    if not arr:
        return []
    if len(arr) == 1:
        return [arr[0], 0]
    if len(arr) == 2:
        if arr[0] % 2 == 0:
            return [arr[0], 0]
        else:
            return [arr[1], 1]
    if len(arr) == 3:
        if arr[0] % 2 == 0:
            return [arr[0], 0]
        elif arr[1] % 2 == 0:
            return [arr[1], 1]
        else:
            return [arr[2], 2]
    if len(arr) == 4:
        if arr[0] % 2 == 0:
            return [arr[0], 0]
        elif arr[1] % 2 == 0:
            return [arr[1], 1]
        elif arr[2] % 2 == 0:
            return [arr[2], 2]
        else:
            return [arr[3], 3]
    if len(arr) == 5:
        if arr[0] % 2 == 0:
            return [arr[0], 0]
        elif arr[1] % 2 == 0:
            return [arr[1], 1]
        elif arr[2] % 2 == 0:
            return [arr[2], 2]
        elif arr[3] % 2 == 0:
            return [arr[3], 3]
        else:
            return [arr[4], 4]


if __name__ == "__main__":
    print(pluck([4, 2, 3]))
    print(pluck([1, 2, 3]))
    print(pluck([]))
    print(pluck([5, 0, 3, 0, 4, 2]))
    print(pluck([5, 0, 3, 0, 4, 2, 1]))
