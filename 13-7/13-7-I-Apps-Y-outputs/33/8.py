
def solve(s, q):
    # Initialize an empty dictionary to store the number of occurrences of each character
    char_count = {}
    
    # Loop through each query
    for query in q:
        # If the query is of type 1, replace the character at the given position with the new character
        if query[0] == 1:
            pos, c = query[1], query[2]
            s = s[:pos] + c + s[pos+1:]
        # If the query is of type 2, count the number of distinct characters in the substring
        else:
            l, r = query[1], query[2]
            # Loop through each character in the substring
            for c in s[l-1:r]:
                # If the character is not already in the dictionary, add it to the dictionary with a count of 1
                if c not in char_count:
                    char_count[c] = 1
                # Otherwise, increment the count of the character
                else:
                    char_count[c] += 1
    
    # Return the number of distinct characters in the substring
    return len(char_count)

