
def solve(n, m, roads, q, transportation_plan):
    # Initialize a dictionary to store the distances between each pair of cities
    distances = {}
    for road in roads:
        city1, city2, length = road
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        distances[city1][city2] = length
        distances[city2][city1] = length

    # Fill in the remaining distances using the bitwise OR operation
    for city1 in distances:
        for city2 in distances[city1]:
            for city3 in distances[city1]:
                if city3 != city2:
                    distances[city1][city3] = distances[city1][city2] | distances[city2][city3]
                    distances[city3][city1] = distances[city1][city2] | distances[city2][city3]

    # Calculate the transportation cost for each day
    transportation_cost = []
    for day in range(q):
        city1, city2 = transportation_plan[day]
        transportation_cost.append(distances[city1][city2])

    return transportation_cost

