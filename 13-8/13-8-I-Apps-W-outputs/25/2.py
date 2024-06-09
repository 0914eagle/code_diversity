
def solve(n, b):
    # Convert the list of integers to a set to remove duplicates
    b_set = set(b)
    # Initialize a list to store the permutation
    permutation = []
    # Iterate through the set of integers
    for i in b_set:
        # Check if the current integer is not already in the permutation
        if i not in permutation:
            # Add the current integer to the permutation
            permutation.append(i)
    # Check if the permutation is valid
    if len(permutation) == len(b_set):
        return "Yes\n" + " ".join(map(str, permutation))
    else:
        return "No"

