
def solve(n, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum discomfort to infinity
    min_discomfort = float('inf')
    # Initialize the resulting array to be empty
    result = []
    # Iterate over all possible starting points
    for i in range(n):
        # Calculate the discomfort of the current circle
        discomfort = calculate_discomfort(arr, i)
        # If the current circle has less discomfort than the minimum discomfort, update the minimum discomfort and the resulting array
        if discomfort < min_discomfort:
            min_discomfort = discomfort
            result = arr[:]
    # Return the resulting array
    return result

def calculate_discomfort(arr, start):
    # Initialize the discomfort to zero
    discomfort = 0
    # Iterate over all elements in the array
    for i in range(len(arr)):
        # Calculate the absolute difference between the current element and the next element
        diff = abs(arr[i] - arr[(i+1)%len(arr)])
        # Add the absolute difference to the discomfort
        discomfort += diff
    # Return the discomfort
    return discomfort

