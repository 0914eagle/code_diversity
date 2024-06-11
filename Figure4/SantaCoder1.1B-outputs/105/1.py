def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [name for name, _ in sorted(zip(names, range(10)))]
    return arr


if __name__ == '__main__':
    print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
    print(by_length([1, 1, 2, 2, 3, 4, 5, 8]))
    print(by_length([]))