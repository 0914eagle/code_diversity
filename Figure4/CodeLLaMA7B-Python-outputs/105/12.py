def by_length(arr):
    
    # O(nlogn)
    # return [str(i) for i in sorted(arr, reverse=True)]

    # O(n)
    return [str(i) for i in sorted(arr, reverse=True) if 1 <= i <= 9]


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
