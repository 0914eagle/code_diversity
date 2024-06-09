
def get_k_incremental_double_free_string(k, n):
    import itertools
    
    # Generate all possible strings of length k
    strings = [''.join(p) for p in itertools.product(list(range(26)), repeat=k)]
    
    # Filter out strings that are not double free
    double_free_strings = []
    for string in strings:
        if all(string[i] != string[i+1] for i in range(len(string)-1)):
            double_free_strings.append(string)
    
    # Filter out strings that are not k-incremental
    k_incremental_strings = []
    for string in double_free_strings:
        char_counts = [string.count(c) for c in string]
        if all(char_counts[i] == i+1 for i in range(len(char_counts))):
            k_incremental_strings.append(string)
    
    # Return the nth string in the alphabetized list
    return k_incremental_strings[n-1] if n <= len(k_incremental_strings) else -1

