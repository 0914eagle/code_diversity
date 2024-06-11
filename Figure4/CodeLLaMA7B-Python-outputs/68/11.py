def pluck(arr):
    
    if not arr:
        return []

    min_value = min(arr)
    min_index = arr.index(min_value)

    if min_value % 2 == 0:
        return [min_value, min_index]

    return []


if __name__ == "__main__":
    print(pluck([4, 2, 3]))
    print(pluck([1, 2, 3]))
    print(pluck([]))
    print(pluck([5, 0, 3, 0, 4, 2]))
