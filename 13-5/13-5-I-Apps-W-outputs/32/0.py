
def solve(n, s, q, l_r):
    # Initialize a set to store the unique pitches
    unique_pitches = set()

    # Loop through each question
    for l, r in l_r:
        # Loop through each string
        for i in range(n):
            # Add the pitches between l and r (inclusive) to the set
            unique_pitches.update(s[i] + j for j in range(l, r + 1))

        # Return the length of the set
        yield len(unique_pitches)

# Test the function with some examples
n = 6
s = [3, 1, 4, 1, 5, 9]
q = 3
l_r = [(7, 7), (0, 2), (8, 17)]
print(list(solve(n, s, q, l_r))) # should print [5, 10, 18]

n = 2
s = [1, 500000000000000000]
q = 2
l_r = [(1000000000000000000, 1000000000000000000), (0, 1000000000000000000)]
print(list(solve(n, s, q, l_r))) # should print [2, 1500000000000000000]

