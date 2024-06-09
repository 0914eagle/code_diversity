
def find_missing_number(n, arr):
    # Sort the array
    arr.sort()

    # Check if the array is already an arithmetic progression
    if arr[0] + (n - 1) * 2 == arr[n - 1]:
        return -1

    # Find the common difference between the numbers
    common_diff = (arr[n - 1] - arr[0]) // (n - 1)

    # Find the missing number
    missing_number = arr[0] + common_diff * (n - 1)

    return missing_number

