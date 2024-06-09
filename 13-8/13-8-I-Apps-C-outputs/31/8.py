
def shortest_distance(planets):
    # Calculate the total distance traveled by visiting each planet once and returning to the home planet
    total_distance = 0
    for planet in planets:
        total_distance += calculate_distance(planet, planets[0])

    # Return the total distance
    return total_distance

def calculate_distance(current_planet, destination_planet):
    # Calculate the Euclidean distance between the current planet and the destination planet
    distance = ((current_planet[0] - destination_planet[0]) ** 2 + (current_planet[1] - destination_planet[1]) ** 2 + (current_planet[2] - destination_planet[2]) ** 2) ** 0.5

    # Return the distance
    return distance

# Main
if __name__ == "__main__":
    # Read the number of planets from stdin
    n = int(input())

    # Read the positions of the planets from stdin
    planets = []
    for i in range(n):
        planet = [int(x) for x in input().split()]
        planets.append(planet)

    # Calculate the shortest distance and print the result
    print(shortest_distance(planets))

