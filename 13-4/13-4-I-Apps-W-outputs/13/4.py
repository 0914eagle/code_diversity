
def solve(n, m, f, b):
    # Initialize a dictionary to store the counts of each number
    counts = {}
    for i in range(n):
        counts[i+1] = 0
    # Loop through the b sequence and increment the count of each number
    for i in range(m):
        counts[b[i]] += 1
    # Check if the counts of each number are the same as the f sequence
    for i in range(n):
        if counts[f[i]] != 1:
            return "Impossible"
    # If all counts are the same, find the original sequence
    a = [0] * m
    for i in range(m):
        a[i] = f.index(b[i]) + 1
    return "Possible\n" + " ".join(map(str, a))

