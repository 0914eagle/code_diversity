
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
        query_type, *query_params = query.split()
        if query_type == "2":
            l, r = map(int, query_params)
            distinct_chars = len(set(s[l-1:r]))
            print(distinct_chars)
        else:
            pos, char = map(str, query_params)
            s = s[:int(pos)-1] + char + s[int(pos):]
            char_count[char] += 1
            char_count[s[int(pos)-1]] -= 1
            if char_count[s[int(pos)-1]] == 0:
                del char_count[s[int(pos)-1]]
    return s

