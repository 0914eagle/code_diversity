
def solve(s, b):
    n = len(s)
    m = len(b)
    if n == m:
        return s
    
    # initialize a dictionary to store the count of each character in s
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # initialize a list to store the characters in s in sorted order
    sorted_chars = sorted(s)
    
    # initialize a list to store the indices of the characters in s
    char_indices = [i for i in range(n)]
    
    # sort the characters in s in descending order
    sorted_chars.reverse()
    
    # initialize a list to store the indices of the characters in t
    t_indices = []
    
    # iterate through the characters in s and their indices
    for i, char in enumerate(s):
        # if the character is not in t_indices, add it to t_indices
        if char not in t_indices:
            t_indices.append(char_indices[i])
    
    # sort t_indices in ascending order
    t_indices.sort()
    
    # initialize a list to store the characters in t
    t = []
    
    # iterate through the characters in s and their indices
    for i, char in enumerate(s):
        # if the character is in t_indices, add it to t
        if char in t_indices:
            t.append(char)
    
    # return t
    return "".join(t)

