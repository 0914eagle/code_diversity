def maximum(arr, k):
    
    if not arr:
        return []

    arr.sort()
    return arr[:k]


if __name__ == '__main__':
    print(maximum([-3, -4, 5], 3))
    print(maximum([4, -4, 4], 2))
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))
