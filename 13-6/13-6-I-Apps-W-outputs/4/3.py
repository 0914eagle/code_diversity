
def get_subset_with_max_diff(S):
    # Sort the set in descending order
    S = sorted(S, reverse=True)
    # Initialize the maximum difference and the subset with the maximum difference
    max_diff = 0
    subset = []
    # Iterate over the set and calculate the difference between the maximum and mean of the subset
    for i in range(len(S)):
        subset.append(S[i])
        diff = S[i] - sum(subset) / len(subset)
        if diff > max_diff:
            max_diff = diff
    return max_diff

def solve(queries):
    # Initialize the set and the maximum difference
    S = []
    max_diff = 0
    # Iterate over the queries
    for query in queries:
        # If the query is of type 1, add the number to the set
        if query[0] == 1:
            S.append(query[1])
        # If the query is of type 2, find the subset with the maximum difference and output the maximum difference
        elif query[0] == 2:
            max_diff = get_subset_with_max_diff(S)
            print(max_diff)
    return max_diff

if __name__ == '__main__':
    queries = [[1, 3], [2], [1, 4], [2], [1, 8], [2]]
    solve(queries)

