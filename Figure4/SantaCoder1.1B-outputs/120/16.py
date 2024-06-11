def maximum(arr, k):
    
    # sort the array
    arr.sort()

    # return the maximum k numbers
    return arr[:k]


if __name__ == "__main__":
    arr = [-3,