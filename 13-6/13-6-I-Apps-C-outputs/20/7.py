
def get_suitable_values(coins, k):
    suitable_values = set()
    for i in range(k+1):
        for c in coins:
            if i % c == 0:
                suitable_values.add(i)
    return suitable_values

