
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
    
    # initialize a list to store the characters in s in the correct order
    char_list = []
    for i in range(n):
        char_list.append(s[i])
    
    # sort the characters in char_list based on their count and index
    char_list.sort(key=lambda x: (char_count[x], x))
    
    # construct the string t by taking the first m characters from char_list
    t = ""
    for i in range(m):
        t += char_list[i]
    
    return t

