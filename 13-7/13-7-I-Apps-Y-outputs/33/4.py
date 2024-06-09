
def solve(s, queries):
    # Initialize a dictionary to store the count of each character in the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    # Iterate over the queries and process them accordingly
    for query in queries:
        if query[0] == 1:
            # Query is of type 1, replace the character at the given position with the new character
            pos, char = query[1], query[2]
            s = s[:pos] + char + s[pos+1:]
            char_count[char] += 1
            char_count[s[pos]] -= 1
        else:
            # Query is of type 2, calculate the number of distinct characters in the substring
            l, r = query[1], query[2]
            distinct_chars = len(set(s[l-1:r]))
            print(distinct_chars)

    return s

