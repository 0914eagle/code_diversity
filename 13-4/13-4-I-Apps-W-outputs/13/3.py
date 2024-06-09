
def solve(n, m, f, b):
    # Initialize a dictionary to store the counts of each number
    counts = {}
    for i in range(n):
        counts[i+1] = 0
    # Iterate through the sequence b and increment the count of each number
    for i in range(m):
        counts[b[i]] += 1
    # Check if the count of each number is equal to the number of times it appears in the sequence b
    for i in range(n):
        if counts[i+1] != f.count(i+1):
            return "Impossible"
    # If all counts are equal, then the sequence a exists and is unique
    a = [0] * m
    for i in range(m):
        a[i] = f.index(b[i]) + 1
    return "Possible\n" + " ".join(map(str, a))

