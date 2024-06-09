
def get_number_of_lit_flats(n, m, windows):
    # Initialize a set to store the indices of lit flats
    lit_flats = set()

    # Iterate over the windows of each floor
    for i in range(n):
        for j in range(m):
            # Check if the current window has lights on
            if windows[i][j] == "1":
                # Add the index of the current flat to the set of lit flats
                lit_flats.add(j)

    # Return the number of lit flats
    return len(lit_flats)

