
def solve(s, q):
    # Initialize a dictionary to store the number of occurrences of each character in the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Iterate through the queries and process them accordingly
    for query in q:
        query_type, pos, c = query
        if query_type == 1:
            # Replace the character at position pos with c
            s = s[:pos] + c + s[pos+1:]
            # Update the character count dictionary
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
            char_count[s[pos]] -= 1
        else:
            # Calculate the number of distinct characters in the substring s[l:r+1]
            l, r = pos
            distinct_chars = len(set(s[l:r+1]))
            print(distinct_chars)

    return s, char_count

