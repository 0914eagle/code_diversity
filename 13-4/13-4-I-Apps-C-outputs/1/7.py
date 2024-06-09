
def get_k_incremental_double_free_string(k, n):
    
    import itertools
    
    # Generate all possible strings of length k
    strings = [''.join(s) for s in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=k)]
    
    # Filter out strings that are not k-incremental or double free
    filtered_strings = []
    for string in strings:
        if is_k_incremental(string, k) and is_double_free(string):
            filtered_strings.append(string)
    
    # Return the nth string in the filtered list
    if n <= len(filtered_strings):
        return filtered_strings[n-1]
    else:
        return -1

def is_k_incremental(string, k):
    
    counts = [0] * 26
    for char in string:
        counts[ord(char) - ord('a')] += 1
    for i in range(1, k+1):
        if counts.count(i) != 1:
            return False
    return True

def is_double_free(string):
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

