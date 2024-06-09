
def find_symmetric_string(n, k, p):
    import itertools
    
    # Check if the requirements are valid
    if n < k or n < p or k < p:
        return "IMPOSSIBLE"
    
    # Generate all possible strings of length n with k distinct characters
    strings = itertools.product(list(range(k)), repeat=n)
    
    # Find the first string that satisfies the requirements
    for string in strings:
        # Check if the string is symmetric
        if string == string[::-1]:
            # Check if the longest palindromic substring has length p
            if max(len(max(string[i:j] for i in range(len(string))) for j in range(len(string), 0, -1))) == p:
                return "".join(chr(ord('a') + s) for s in string)
    
    # If no string satisfies the requirements, return IMPOSSIBLE
    return "IMPOSSIBLE"

