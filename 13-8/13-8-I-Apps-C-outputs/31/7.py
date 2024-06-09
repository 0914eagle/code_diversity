
def solve(n, planets):
    # Calculate the distance between each pair of planets
    distances = {}
    for i in range(n):
        for j in range(i+1, n):
            distances[(i, j)] = distances[(j, i)] = calc_distance(planets[i], planets[j])

    # Use dynamic programming to find the minimum distance for each planet
    min_distances = [0] * n
    for i in range(1, n):
        min_distances[i] = min(min_distances[i-1] + distances[(i-1, i)], min_distances[i-1] + distances[(i, i-1)])

    return min_distances[-1]

def calc_distance(planet1, planet2):
    return ((planet1[0] - planet2[0]) ** 2 + (planet1[1] - planet2[1]) ** 2 + (planet1[2] - planet2[2]) ** 2) ** 0.5

