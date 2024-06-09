
def solve(n, s, q, l_r):
    # Initialize a set to store the unique pitches
    unique_pitches = set()

    # Iterate over each query
    for l, r in l_r:
        # Iterate over each string
        for i in range(n):
            # Add the pitches between l and r (inclusive) to the set
            unique_pitches.update(s[i] + j for j in range(l, r + 1))

        # Return the number of unique pitches
        print(len(unique_pitches))

        # Reset the set for the next query
        unique_pitches = set()

# Test case 1
n = 6
s = [3, 1, 4, 1, 5, 9]
q = 3
l_r = [(7, 7), (0, 2), (8, 17)]
solve(n, s, q, l_r)

# Test case 2
n = 2
s = [1, 500000000000000000]
q = 2
l_r = [(1000000000000000000, 1000000000000000000), (0, 1000000000000000000)]
solve(n, s, q, l_r)

