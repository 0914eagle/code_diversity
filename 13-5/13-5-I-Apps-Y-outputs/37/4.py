
def solve(s, t):
    # Initialize a dictionary to store the number of operations required for each character
    char_ops = {}
    for char in s:
        char_ops[char] = 0
    
    # Iterate through the characters of both strings and update the dictionary
    for i in range(len(s)):
        if s[i] != t[i]:
            char_ops[s[i]] += 1
    
    # Find the minimum number of operations required to change S to T
    min_ops = float('inf')
    for char, ops in char_ops.items():
        if ops < min_ops:
            min_ops = ops
    
    return min_ops

