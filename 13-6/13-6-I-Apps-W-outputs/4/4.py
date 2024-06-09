
def max_mean_subset(S):
    # Calculate the mean of the set S
    mean = sum(S) / len(S)
    # Initialize the maximum difference between the maximum and mean as 0
    max_diff = 0
    # Initialize the subset with the first element of S
    subset = [S[0]]
    # Iterate over the remaining elements of S
    for i in range(1, len(S)):
        # If the current element is greater than the mean, add it to the subset
        if S[i] > mean:
            subset.append(S[i])
        # If the current element is less than the mean, calculate the difference between the maximum and mean of the current subset
        else:
            diff = max(subset) - mean
            # If the difference is greater than the current maximum difference, update the maximum difference and subset
            if diff > max_diff:
                max_diff = diff
                subset = [S[i]]
    # Return the maximum difference and subset
    return max_diff, subset

def process_queries(queries):
    # Initialize an empty set S
    S = []
    # Iterate over the queries
    for query in queries:
        # If the query is of type 1, add the element to S
        if query[0] == 1:
            S.append(query[1])
        # If the query is of type 2, find the maximum mean subset of S and return the difference between the maximum and mean
        else:
            max_diff, subset = max_mean_subset(S)
            print(max_diff)
    return

if __name__ == '__main__':
    queries = [[1, 3], [2], [1, 4], [2], [1, 8], [2]]
    process_queries(queries)

