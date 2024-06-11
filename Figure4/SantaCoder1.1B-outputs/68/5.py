def pluck(arr):
    
    if not arr:
        return []
    arr.sort()
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            return [arr[i], i]
    return []


if __name__ == "__main__":
    print(pluck([4, 2, 3]))
    print(pluck([1, 2, 3]))
    print(pluck([]))
    print(pluck([5, 0, 3, 0, 4, 2]))
