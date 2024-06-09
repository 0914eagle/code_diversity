
def solve(s, q):
    # Initialize an empty dictionary to store the number of occurrences of each character
    char_count = {}
    
    # Loop through each query
    for query in q:
        # If the query is of type 1, replace the character at the given position with the new character
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos] + c + s[pos+1:]
        # If the query is of type 2, calculate the number of distinct characters in the substring and print the answer
        else:
            l, r = query[1], query[2]
            distinct_chars = len(set(s[l-1:r]))
            print(distinct_chars)

