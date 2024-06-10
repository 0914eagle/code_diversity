
import sys
import itertools

def get_tastiness(n, k, t, u):
    # Initialize the tastiness of each combination of flavors
    tastiness = [[0] * (k + 1) for _ in range(k + 1)]
    
    # Populate the tastiness of each combination of flavors
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            tastiness[i][j] = tastiness[i - 1][j - 1] + t[i - 1] + t[j - 1] + u[i - 1][j - 1]
    
    # Initialize the maximum tastiness and the corresponding number of scoops
    max_tastiness = 0
    num_scoops = 0
    
    # Iterate over all possible combinations of flavors
    for combination in itertools.combinations(range(1, k + 1), n):
        # Calculate the tastiness of this combination
        tastiness_combination = sum(tastiness[i][i] for i in combination)
        
        # If the tastiness of this combination is greater than the current maximum, update the maximum and the number of scoops
        if tastiness_combination > max_tastiness:
            max_tastiness = tastiness_combination
            num_scoops = len(combination)
    
    # Return the maximum tastiness and the corresponding number of scoops
    return max_tastiness, num_scoops

def get_cost(n, k, a, b):
    # Calculate the cost of the ice cream
    cost = n * a + b
    
    # Return the cost
    return cost

def get_tastiness_per_gold_coin_ratio(n, k, t, u, a, b):
    # Calculate the maximum tastiness and the number of scoops
    max_tastiness, num_scoops = get_tastiness(n, k, t, u)
    
    # Calculate the cost
    cost = get_cost(num_scoops, k, a, b)
    
    # Calculate the tastiness per gold coin ratio
    tastiness_per_gold_coin_ratio = max_tastiness / cost
    
    # Return the tastiness per gold coin ratio
    return tastiness_per_gold_coin_ratio

if __name__ == '__main__':
    n, k, a, b = map(int, input().split())
    t = list(map(int, input().split()))
    u = []
    for i in range(k):
        u.append(list(map(int, input().split())))
    print(get_tastiness_per_gold_coin_ratio(n, k, t, u, a, b))

