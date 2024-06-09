
def solve(s, queries):
    # Initialize a dictionary to store the number of occurrences of each character in the string
    char_counts = {}
    for char in s:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    # Iterate through the queries and process them accordingly
    for query in queries:
        if query[0] == 1:  # Query of type 1: replace character at position pos with character c
            pos, c = query[1], query[2]
            s = s[:pos] + c + s[pos+1:]
            char_counts[c] += 1
            char_counts[s[pos]] -= 1
            if char_counts[s[pos]] == 0:
                del char_counts[s[pos]]
        else:  # Query of type 2: count the number of distinct characters in the substring s[l:r+1]
            l, r = query[1], query[2]
            print(len(set(s[l:r+1])))

s = "abacaba"
queries = [[2, 1, 4], [1, 4, "b"], [1, 5, "b"], [2, 4, 6], [2, 1, 7]]
solve(s, queries)

s = "dfcbbcfeeedbaea"
queries = [[1, 6, "e"], [1, 4, "b"], [2, 6, 14], [1, 7, "b"], [1, 12, "c"], [2, 6, 8], [2, 1, 6], [1, 7, "c"], [1, 10, "a"], [2, 7, 9], [1, 10, "a"], [1, 14, "b"], [1, 1, "f"], [2, 1, 11]]
solve(s, queries)

