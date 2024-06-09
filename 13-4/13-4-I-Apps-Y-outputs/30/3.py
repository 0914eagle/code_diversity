
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the number of operations to 0
    operations = 0
    # Loop through the array and divide each element by 2 rounding down
    for i in range(n):
        arr[i] //= 2
        operations += 1
    # Return the number of operations required
    return operations

