
def solve(n, arr):
    # Convert the array to a set to remove duplicates
    unique_elements = set(arr)
    # Check if the largest element is present in the array
    if 11 in unique_elements:
        return 11
    # Check if the second largest element is present in the array
    if 10 in unique_elements:
        return 10
    # Check if the third largest element is present in the array
    if 9 in unique_elements:
        return 9
    # Check if the fourth largest element is present in the array
    if 8 in unique_elements:
        return 8
    # If none of the above conditions are met, return 0
    return 0

