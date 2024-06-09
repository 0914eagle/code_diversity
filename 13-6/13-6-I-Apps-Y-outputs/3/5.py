
def solve(n, r, arr):
    # Sort the array and find the maximum range that can be warmed up
    arr.sort()
    max_range = 0
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > max_range:
            max_range = arr[i + 1] - arr[i]

    # If the maximum range is greater than or equal to the radius, return the number of heaters needed
    if max_range >= r:
        return n

    # If the maximum range is less than the radius, return -1
    return -1

