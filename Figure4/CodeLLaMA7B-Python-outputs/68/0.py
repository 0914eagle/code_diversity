def pluck(arr):
    
    if not arr:
        return []
    min_val = min(arr)
    min_index = arr.index(min_val)
    if min_val % 2 == 0:
        return [min_val, min_index]
    else:
        return []


if __name__ == "__main__":
    print(pluck([4,2,3]))
    print(pluck([1,2,3]))
    print(pluck([]))
    print(pluck([5, 0, 3, 0, 4, 2]))
