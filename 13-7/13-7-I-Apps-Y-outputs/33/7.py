
def solve(s, queries):
    # Initialize a dictionary to store the count of each character in the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Iterate over the queries and process them according to their type
    for query in queries:
        if query[0] == 1:
            # Query type 1: Replace the character at the given position with the given character
            pos, char = query[1], query[2]
            s = s[:pos] + char + s[pos+1:]
            char_count[char] += 1
            char_count[s[pos]] -= 1
            if char_count[s[pos]] == 0:
                del char_count[s[pos]]
        else:
            # Query type 2: Calculate the number of distinct characters in the substring
            l, r = query[1], query[2]
            print(len(set(s[l-1:r])))
            
            
s = "abacaba"
queries = [(2, 1, 4), (1, 4, "b"), (1, 5, "b"), (2, 4, 6), (2, 1, 7)]
solve(s, queries)

s = "dfcbbcfeeedbaea"
queries = [(1, 6, "e"), (1, 4, "b"), (2, 6, 14), (1, 7, "b"), (1, 12, "c"), (2, 6, 8), (2, 1, 6), (1, 7, "c"), (1, 10, "a"), (2, 7, 9), (1, 10, "a"), (1, 14, "b"), (1, 1, "f"), (2, 1, 11)]
solve(s, queries)

