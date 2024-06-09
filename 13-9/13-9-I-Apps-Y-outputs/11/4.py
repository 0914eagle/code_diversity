
def solve(n, arr):
    # Find the largest element in the array
    largest = max(arr)

    # Find the index of the largest element
    largest_index = arr.index(largest)

    # Return the index of the largest element + 1
    return largest_index + 1

