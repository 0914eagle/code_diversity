
def solve(s, q):
    # Initialize a dictionary to store the number of occurrences of each character in the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Iterate through the queries and print the answer for each query of the second type
    for query in q:
        if query[0] == 2:
            l, r = query[1], query[2]
            # Get the subset of the string between indices l and r
            subset = s[l-1:r]
            # Initialize a set to store the unique characters in the subset
            unique_chars = set()
            for char in subset:
                unique_chars.add(char)
            # Print the number of unique characters in the subset
            print(len(unique_chars))
        else:
            pos, char = query[1], query[2]
            # Update the character at position pos in the string
            s = s[:pos-1] + char + s[pos:]
            # Update the character count dictionary
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

