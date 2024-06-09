
def solve(s, t):
    # Initialize a dictionary to store the number of operations required for each character
    char_ops = {}
    for char in s:
        char_ops[char] = 0
    
    # Iterate through the characters of both strings and calculate the number of operations required for each character
    for i in range(len(s)):
        if s[i] != t[i]:
            char_ops[s[i]] += 1
    
    # Find the character with the minimum number of operations required and return it
    min_ops = min(char_ops.values())
    for char, ops in char_ops.items():
        if ops == min_ops:
            return min_ops

