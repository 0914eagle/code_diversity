
def solve(n, arr):
    # convert the array to a set to remove duplicates
    unique_elements = set(arr)
    # sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    # initialize a variable to store the largest number of unique elements
    max_unique_elements = 0
    # loop through the array and check if the current number of unique elements is greater than the largest number of unique elements so far
    for i in range(n):
        if len(unique_elements) > max_unique_elements:
            max_unique_elements = len(unique_elements)
        # remove the current number from the set of unique elements
        unique_elements.remove(sorted_arr[i])
    # return the largest number of unique elements
    return max_unique_elements

