
import math

def get_min_distance(planets):
    # Calculate the distance between each pair of planets
    distances = {}
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            distance = math.sqrt(sum((planets[i] - planets[j])**2))
            distances[(i, j)] = distance

    # Use a dynamic programming approach to find the minimum distance
    memo = {(0, 0): 0}
    for i in range(1, len(planets)):
        memo[(i, i)] = 0
        for j in range(i):
            memo[(i, j)] = min(memo[(i, j)], memo[(i-1, j)] + distances[(j, i)])
            memo[(j, i)] = min(memo[(j, i)], memo[(i, j)])

    return memo[(len(planets)-1, 0)]

planets = [(0, 0, 1), (0, 1, 1), (2, 0, 3), (2, 1, 3)]
print(get_min_distance(planets))

