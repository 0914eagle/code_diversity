
def get_minimal_bdd_size(n, function):
    # Initialize the BDD with a single vertex
    bdd = [0]

    # Iterate over the input values
    for i in range(2**n):
        # Get the current value of the function for this input
        value = function[i]

        # If the value is 0, skip this input
        if value == 0:
            continue

        # If the value is 1, add a new vertex to the BDD
        bdd.append(len(bdd))

    # Return the size of the BDD
    return len(bdd)

