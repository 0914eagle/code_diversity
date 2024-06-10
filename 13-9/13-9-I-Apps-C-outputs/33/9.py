
import sys
import math

def max_tastiness(n, k, a, b, tastiness, complementary_tastiness):
    # Initialize the maximum tastiness and the corresponding combination of scoops
    max_tastiness = 0
    scoops = []
    
    # Loop through each possible combination of scoops
    for i in range(1, n + 1):
        for combination in combinations(range(k), i):
            # Calculate the tastiness of the current combination of scoops
            current_tastiness = sum(tastiness[i] for i in combination)
            
            # Check if the current combination of scoops is complementary
            complementary = all(complementary_tastiness[i][j] >= 0 for i in combination for j in combination if i != j)
            
            # If the current combination of scoops is complementary and has a higher tastiness than the previous maximum, update the maximum tastiness and the corresponding combination of scoops
            if complementary and current_tastiness > max_tastiness:
                max_tastiness = current_tastiness
                scoops = combination
    
    # Calculate the cost of the ice cream
    cost = a * len(scoops) + b
    
    # Return the maximum possible tastiness per gold coin ratio
    return max_tastiness / cost

def combinations(iterable, r):
    # combinations('abc', 2) --> ('ab', 'ac', 'bc')
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i:] = list(range(i + 1, i + n - r + 1))
        yield tuple(pool[i] for i in indices)

if __name__ == '__main__':
    n, k, a, b = map(int, input().split())
    tastiness = list(map(int, input().split()))
    complementary_tastiness = [[0] * k for _ in range(k)]
    for i in range(k):
        complementary_tastiness[i] = list(map(int, input().split()))
    print(max_tastiness(n, k, a, b, tastiness, complementary_tastiness))

