def by_length(arr):
    
    if not arr:
        return []
    arr.sort()
    arr = [name for name in names if name in arr]
    arr.reverse()
    return arr


if __name__ == "__main__":
    print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
    print(by_length([1, -1, 55]))
    print(by_length([]))
    print(by_length([1, 2, 3, 4, 