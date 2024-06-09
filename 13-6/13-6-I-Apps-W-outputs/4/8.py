
def get_max_mean_subset(S):
    # Sort the set in descending order
    S = sorted(S, reverse=True)
    # Initialize the maximum mean
    max_mean = 0
    # Initialize the current subset
    curr_subset = []
    # Initialize the current sum
    curr_sum = 0
    # Iterate over the set
    for num in S:
        # If the current sum plus the current number is less than or equal to the maximum mean, add the number to the current subset
        if curr_sum + num <= max_mean:
            curr_subset.append(num)
            curr_sum += num
        # If the current sum plus the current number is greater than the maximum mean, add the number to the current subset and update the maximum mean
        else:
            curr_subset.append(num)
            max_mean = curr_sum + num
            curr_sum = num
    # Return the maximum mean
    return max_mean

def solve(queries):
    # Initialize the set
    S = set()
    # Iterate over the queries
    for query in queries:
        # If the query is of type 1, add the number to the set
        if query[0] == 1:
            S.add(query[1])
        # If the query is of type 2, find the maximum mean subset and return the maximum mean
        elif query[0] == 2:
            return get_max_mean_subset(S)
    # Return the maximum mean
    return get_max_mean_subset(S)

if __name__ == '__main__':
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    print(solve(queries))

