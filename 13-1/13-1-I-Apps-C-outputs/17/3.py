
def get_min_cost(planets):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop through all pairs of planets
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            # Calculate the cost of the tunnel between the two planets
            cost = abs(planets[i][0] - planets[j][0]) + abs(planets[i][1] - planets[j][1]) + abs(planets[i][2] - planets[j][2])
            
            # Update the minimum cost if necessary
            if cost < min_cost:
                min_cost = cost
    
    return min_cost

def main():
    # Read the number of planets and their coordinates from stdin
    num_planets = int(input())
    planets = []
    for _ in range(num_planets):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    
    # Calculate the minimum cost of forming the network of tunnels
    min_cost = get_min_cost(planets)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

