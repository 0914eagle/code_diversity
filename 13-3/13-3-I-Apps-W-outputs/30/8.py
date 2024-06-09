
def solve(n, b):
    # Convert the list of integers to a set to remove duplicates
    b_set = set(b)
    # Initialize a list to store the permutation
    permutation = []
    # Iterate through the set of integers
    for i in b_set:
        # Check if the current integer is already in the permutation
        if i not in permutation:
            # If not, add it to the permutation
            permutation.append(i)
    # Check if the permutation is valid
    if len(permutation) == len(b_set):
        return "Yes\n" + " ".join(str(i) for i in permutation)
    else:
        return "No"
