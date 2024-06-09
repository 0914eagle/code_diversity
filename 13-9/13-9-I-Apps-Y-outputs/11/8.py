
def solve(n, arr):
    # Find the largest element in the array
    largest = max(arr)

    # Find the number of elements that are equal to the largest element
    count = arr.count(largest)

    # Return the number of elements that are equal to the largest element
    return count

