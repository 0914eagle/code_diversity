
def solve(n, m, windows):
    # Initialize a set to store the indices of flats with lights on
    lit_flats = set()

    # Iterate over the windows of each floor
    for i in range(n):
        for j in range(0, 2 * m, 2):
            # If the window has lights on, add the corresponding flat index to the set
            if windows[i][j] == "1" or windows[i][j + 1] == "1":
                lit_flats.add(j // 2 + 1)

    # Return the number of flats with lights on
    return len(lit_flats)

