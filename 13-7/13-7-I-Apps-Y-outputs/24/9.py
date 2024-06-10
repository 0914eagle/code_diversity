
def get_min_coins(coins, value):
    # Initialize a dictionary to store the minimum number of coins needed for each value
    min_coins = {0: 0}
    for coin in coins:
        min_coins[coin] = 1
    
    # Loop through the values and calculate the minimum number of coins needed for each value
    for value in range(1, max(coins) * 2):
        for coin in coins:
            if value >= coin:
                min_coins[value] = min(min_coins[value], min_coins[value - coin] + 1)
            else:
                break
    
    return min_coins[value]

def solve(coins, queries):
    # Initialize a list to store the answers
    answers = []
    
    # Loop through the queries and calculate the minimum number of coins needed for each query
    for query in queries:
        answers.append(get_min_coins(coins, query))
    
    return answers

if __name__ == '__main__':
    n, q = map(int, input().split())
    coins = list(map(int, input().split()))
    queries = [int(input()) for _ in range(q)]
    answers = solve(coins, queries)
    for answer in answers:
        print(answer)

