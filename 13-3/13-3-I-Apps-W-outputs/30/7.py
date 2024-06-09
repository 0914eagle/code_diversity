
def solve(n, b):
    # Check if the sequence is strictly increasing
    for i in range(1, n):
        if b[i] <= b[i-1]:
            return "No"
    
    # Check if the sequence is a permutation of the original sequence
    b = sorted(b)
    for i in range(n):
        if b[i] != i+1:
            return "No"
    
    # If the sequence is valid, return it
    return "Yes\n" + " ".join(str(x) for x in b)

