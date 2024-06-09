
def solve(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize a set to store the unique elements in the array
    unique_elements = set()
    # Iterate through the array
    for element in a:
        # If the element is not already in the set, add it to the set
        if element not in unique_elements:
            unique_elements.add(element)
    # Return True if there is only one element in the set, otherwise return False
    return len(unique_elements) == 1

