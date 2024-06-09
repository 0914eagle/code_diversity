
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
        query_type, *query_params = query.split()
        if query_type == "1":
            # Replace the character at the given position with the new character
            pos, char = int(query_params[0]), query_params[1]
            s = s[:pos] + char + s[pos+1:]
            char_count[char] += 1
            char_count[s[pos]] -= 1
            if char_count[s[pos]] == 0:
                del char_count[s[pos]]
        elif query_type == "2":
            # Calculate the number of distinct characters in the substring
            l, r = int(query_params[0]), int(query_params[1])
            distinct_chars = len(set(s[l:r+1]))
            print(distinct_chars)
        else:
            raise ValueError("Invalid query type")

