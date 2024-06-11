def pluck(arr):
    
    if not arr:
        return []

    min_even = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] % 2 == 0:
            min_even = arr[i]
            min_index = i

    return [min_even, min_index]


if __name__ == "__main__":
    print(pluck([4, 2, 3]))
    print(pluck([1, 2, 3]))
    print(pluck([]))
    print(pluck([5, 0, 3, 0, 4, 2]))
