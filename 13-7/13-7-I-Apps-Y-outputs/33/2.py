
def solve(s, q):
    # Initialize a dictionary to store the number of occurrences of each character in the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    # Iterate through the queries
    for query in q:
        # If the query is of type 1, replace the character at the given position with the new character
        if query[0] == 1:
            pos, char = query[1], query[2]
            s = s[:pos] + char + s[pos+1:]
            char_count[char] += 1
            char_count[s[pos]] -= 1
            if char_count[s[pos]] == 0:
                del char_count[s[pos]]
        # If the query is of type 2, calculate the number of distinct characters in the substring
        else:
            l, r = query[1], query[2]
            print(len(set(s[l-1:r])))

solve(input(), input())

