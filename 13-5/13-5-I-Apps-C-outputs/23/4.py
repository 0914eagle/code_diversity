
def find_sequence(n, k):
    if k > n or k < 1:
        return -1
    
    sequence = list(range(1, n+1))
    for i in range(n):
        if sequence[i] != i+1:
            sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    
    return sequence

