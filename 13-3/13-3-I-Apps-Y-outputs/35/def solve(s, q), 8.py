
def solve(s, q):
    # Initialize a dictionary to store the number of occurrences of each character in the string
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    
    # Iterate through the queries and process them accordingly
    for query in q:
        if query[0] == 1: # Replace character at position pos with character c
            pos, c = query[1], query[2]
            s = s[:pos] + c + s[pos+1:]
            char_count[c] += 1
            char_count[s[pos]] -= 1
            if char_count[s[pos]] == 0:
                del char_count[s[pos]]
        else: # Calculate the number of distinct characters in the substring s[l:r+1]
            l, r = query[1], query[2]
            print(len(set(s[l:r+1])))

