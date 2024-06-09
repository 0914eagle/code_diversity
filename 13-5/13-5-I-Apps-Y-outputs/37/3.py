
def solve(s, t):
    # Initialize a dictionary to store the number of operations required for each character
    d = {}
    for i in range(len(s)):
        d[s[i]] = i + 1
    
    # Initialize a variable to store the minimum number of operations required
    min_ops = len(s)
    
    # Iterate over the characters of T
    for i in range(len(t)):
        # If the current character of T is not in S, skip it
        if t[i] not in s:
            continue
        
        # If the current character of T is in S, find the index of the corresponding character in S
        index = d[t[i]]
        
        # Calculate the number of operations required to replace the current character of T with the corresponding character in S
        ops = index - i
        
        # Update the minimum number of operations required if the current number of operations is less than the minimum
        if ops < min_ops:
            min_ops = ops
    
    return min_ops

