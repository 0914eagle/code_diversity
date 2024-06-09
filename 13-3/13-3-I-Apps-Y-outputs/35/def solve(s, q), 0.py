
def solve(s, q):
    # Initialize a dictionary to store the number of occurrences of each character in the string
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
            # Calculate the number of distinct characters in the substring s[l:r+1]
            l, r = pos
            distinct_chars = len(set(s[l:r+1]))
            print(distinct_chars)

solve("abacaba", [[2, 1, 4], [1, 4, "b"], [1, 5, "b"], [2, 4, 6], [2, 1, 7]])
solve("dfcbbcfeeedbaea", [[1, 6, "e"], [1, 4, "b"], [2, 6, 14], [1, 7, "b"], [1, 12, "c"], [2, 6, 8], [2, 1, 6], [1, 7, "c"], [1, 2, "f"], [1, 10, "a"], [2, 7, 9], [1, 10, "a"], [1, 14, "b"], [1, 1, "f"], [2, 1, 11]])

