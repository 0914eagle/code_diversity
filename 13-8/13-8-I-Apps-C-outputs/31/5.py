
def solve(n, planets):
    # Calculate the total distance traveled by visiting each planet and returning to the home planet
    total_distance = 0
    for i in range(n):
        current_planet = planets[i]
        for j in range(i+1, n):
            next_planet = planets[j]
            distance = calculate_distance(current_planet, next_planet)
            total_distance += distance
    return total_distance

def calculate_distance(planet1, planet2):
    # Calculate the Euclidean distance between two planets
    return ((planet1[0] - planet2[0]) ** 2 + (planet1[1] - planet2[1]) ** 2 + (planet1[2] - planet2[2]) ** 2) ** 0.5

