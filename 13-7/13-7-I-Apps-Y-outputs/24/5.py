
def get_min_coins(values, target):
    # Initialize the memoization dictionary
    memo = {0: 0}
    
    # Iterate over the values in descending order
    for value in sorted(values, reverse=True):
        # Check if the value is already in the memoization dictionary
        if value not in memo:
            # If not, calculate the minimum number of coins needed to reach the value
            memo[value] = 1 + memo[target - value] if target - value in memo else float('inf')
    
    # Return the minimum number of coins needed to reach the target
    return memo[target]

def get_coins(values, target):
    # Initialize the memoization dictionary
    memo = {}
    
    # Iterate over the values in descending order
    for value in sorted(values, reverse=True):
        # Check if the value is already in the memoization dictionary
        if value not in memo:
            # If not, calculate the minimum number of coins needed to reach the value
            memo[value] = 1 + memo[target - value] if target - value in memo else float('inf')
    
    # Return the minimum number of coins needed to reach the target
    return memo[target]

def main():
    # Read the number of coins and queries
    n, q = map(int, input().split())
    
    # Read the values of the coins
    values = list(map(int, input().split()))
    
    # Read the queries
    queries = [int(input()) for _ in range(q)]
    
    # Initialize the answers
    answers = []
    
    # Iterate over the queries
    for query in queries:
        # Get the minimum number of coins needed to reach the query
        ans = get_min_coins(values, query)
        
        # If the minimum number of coins is not infinite, add the answer to the answers list
        if ans != float('inf'):
            answers.append(ans)
        # Otherwise, add -1 to the answers list
        else:
            answers.append(-1)
    
    # Print the answers
    print(*answers, sep='\n')

if __name__ == '__main__':
    main()

