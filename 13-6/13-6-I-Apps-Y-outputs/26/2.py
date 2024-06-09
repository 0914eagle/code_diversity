
def common_divisors(arr):
    # Convert the array to a set to remove duplicates
    unique_elements = set(arr)
    # Initialize a variable to store the number of common divisors
    num_common_divisors = 0
    # Iterate over the unique elements in the array
    for element in unique_elements:
        # Check if the element is a common divisor of all elements in the array
        if all(element % num == 0 for num in arr):
            num_common_divisors += 1
    return num_common_divisors

