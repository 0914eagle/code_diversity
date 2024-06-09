
def solve(s, q):
    # Initialize an empty dictionary to store the count of distinct characters
    distinct_chars = {}

    # Iterate over each query
    for query in q:
        # If the query is of type 1, replace the character at the given position with the new character
        if query[0] == 1:
            s = s[:query[1]] + query[2] + s[query[1] + 1:]
        # If the query is of type 2, calculate the number of distinct characters in the substring
        else:
            count = 0
            for char in s[query[1] - 1:query[2]]:
                if char not in distinct_chars:
                    count += 1
                    distinct_chars[char] = 1
            print(count)

    return s

