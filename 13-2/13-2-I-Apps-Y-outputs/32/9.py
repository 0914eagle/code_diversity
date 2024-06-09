
def solve(n, arr):
    # find the largest element in the array
    largest = max(arr)
    # find the index of the largest element
    largest_index = arr.index(largest)
    # return the index of the largest element + 1
    return largest_index + 1

