
def find_sequence(n, k):
    if k > n or k < 1:
        return -1
    
    sequence = list(range(1, n+1))
    for i in range(n):
        if sequence[i] != i+1:
            sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    
    if len(max(zip(*[sequence[i:] for i in range(k)]), key=lambda x: x[-1]-x[0])[0]) == k:
        return sequence
    else:
        return -1

