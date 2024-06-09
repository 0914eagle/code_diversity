
def count_distinct_strings(n, m, a, b):
    # Initialize a set to store the distinct strings
    distinct_strings = set()
    
    # Loop through each element in the array b
    for i in range(m):
        # Get the current value of k
        k = b[i]
        
        # Loop through each character in the string
        for j in range(n):
            # If the current character is not already in the set, add it
            if s[j] not in distinct_strings:
                distinct_strings.add(s[j])
    
    # Return the number of distinct strings
    return len(distinct_strings) % 998244353

