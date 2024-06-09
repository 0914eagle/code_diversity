
def solve(N, M, *data):
    # Initialize a set to store the common liked foods
    common_liked_foods = set(range(1, M+1))

    # Iterate over the data
    for i in range(N):
        # Get the liked foods for the current person
        liked_foods = set(data[i])

        # Update the common liked foods
        common_liked_foods &= liked_foods

    # Return the number of common liked foods
    return len(common_liked_foods)

