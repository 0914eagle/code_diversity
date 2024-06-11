def maximum(arr, k):
    
    # sort the array
    arr.sort()
    # return the maximum k elements
    return arr[:k]


if __name__ == '__main__':
    print(maximum([-3