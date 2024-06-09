
def solve(s, q):
    # Initialize a dictionary to store the count of each character in the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Iterate through the queries and calculate the number of distinct characters in the substring
    for query in q:
        query_type, pos, c = query
        if query_type == 1:
            # Replace the character at position pos with c
            s = s[:pos] + c + s[pos+1:]
            char_count[c] += 1
            char_count[s[pos]] -= 1
            if char_count[s[pos]] == 0:
                del char_count[s[pos]]
        else:
            # Calculate the number of distinct characters in the substring
            l, r = pos, c
            distinct_chars = len(set(s[l:r+1]))
            print(distinct_chars)

