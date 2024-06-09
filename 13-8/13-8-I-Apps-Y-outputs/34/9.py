
def get_points(x):
    # Find all possible combinations of k numbers that multiply to x
    combinations = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            combinations.append([i, int(x/i)])
    
    # Find the combination with the maximum number of factors
    max_factors = 0
    for combination in combinations:
        factors = len(set(combination))
        if factors > max_factors:
            max_factors = factors
            optimal_combination = combination
    
    # Return the number of points obtained by the second player
    return len(optimal_combination)

