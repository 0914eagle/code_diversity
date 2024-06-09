
def get_k_incremental_double_free_string(k, n):
    
    import itertools
    
    # Generate all possible strings of length k
    strings = [''.join(p) for p in itertools.product(list(range(1, k+1)), repeat=k)]
    
    # Filter out strings that are not double free
    strings = [s for s in strings if all(s[i] != s[i+1] for i in range(len(s)-1))]
    
    # Filter out strings that are not k-incremental
    strings = [s for s in strings if all(s.count(str(i)) == i for i in range(1, k+1))]
    
    # Return the nth string, if it exists
    if n <= len(strings):
        return strings[n-1]
    
    # Otherwise, return -1
    return -1

