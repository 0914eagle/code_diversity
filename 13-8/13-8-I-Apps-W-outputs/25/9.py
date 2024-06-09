
def solve(n, b):
    # Convert the input list to a set to remove duplicates
    b = set(b)
    # Initialize the output list
    b_perm = []
    # Iterate through the input list
    for i in range(1, n+1):
        # Find the next element in the input list that is not already in the output list
        next_element = next((x for x in b if x not in b_perm), None)
        # If no such element exists, return "No"
        if next_element is None:
            return "No"
        # Add the element to the output list
        b_perm.append(next_element)
        # Remove the element from the input list
        b.remove(next_element)
    # Return "Yes" and the output list
    return "Yes\n" + " ".join(map(str, b_perm))

