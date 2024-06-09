
def get_bdd_size(n, function_values):
    # Initialize the BDD with a single vertex representing the root
    bdd = [0]

    # Iterate over the function values
    for i in range(2**n):
        # Get the current function value
        value = function_values[i]

        # If the value is 0, skip it
        if value == 0:
            continue

        # If the value is 1, add a new vertex to the BDD
        bdd.append(len(bdd))

    # Return the size of the BDD
    return len(bdd)

