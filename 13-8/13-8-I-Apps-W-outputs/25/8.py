
def solve(n, b):
    # First, we need to check if the given sequence is valid
    for i in range(1, n):
        if b[i] <= b[i-1]:
            return "No"
    
    # If the sequence is valid, we can find a permutation by sorting it
    b.sort()
    return "Yes\n" + " ".join(str(x) for x in b)

