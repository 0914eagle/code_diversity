
def solve(n, b):
    # Check if the sequence is strictly increasing
    for i in range(1, n):
        if b[i] <= b[i-1]:
            return "No"
    
    # Check if the sequence is a permutation of the original sequence
    orig_seq = [1]
    for i in range(1, n):
        orig_seq.append(orig_seq[i-1] ^ b[i-1])
    
    if sorted(b) != sorted(orig_seq):
        return "No"
    
    return "Yes\n" + " ".join(map(str, b))

