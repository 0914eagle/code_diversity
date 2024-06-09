
def find_subset(S, n):
    # Sort the set S in non-decreasing order
    S.sort()
    # Initialize the maximum value of max(s) - mean(s)
    max_value = 0
    # Initialize the subset s as an empty set
    s = []
    # Iterate over the elements of S
    for i in range(n):
        # If the current element is greater than the mean of s, include it in the subset s
        if S[i] > sum(s) / len(s):
            s.append(S[i])
        # If the current element is less than the mean of s, exclude it from the subset s
        else:
            s.pop()
        # Calculate the maximum value of max(s) - mean(s)
        max_value = max(max_value, S[i] - sum(s) / len(s))
    # Return the maximum value of max(s) - mean(s)
    return max_value

def solve(queries):
    # Initialize the set S as an empty set
    S = []
    # Iterate over the queries
    for query in queries:
        # If the query is of type 1, add the element to the set S
        if query[0] == 1:
            S.append(query[1])
        # If the query is of type 2, find the subset s of the set S with the maximum value of max(s) - mean(s)
        elif query[0] == 2:
            print(find_subset(S, len(S)))

if __name__ == '__main__':
    queries = [[1, 3], [2], [1, 4], [2], [1, 8], [2]]
    solve(queries)

