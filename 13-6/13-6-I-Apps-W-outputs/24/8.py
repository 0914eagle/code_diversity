
def get_min_cost(cities):
    
    # Initialize the minimum total cost to infinity
    min_cost = float('inf')
    
    # Iterate over all possible subsets of cities
    for byteland_cities, disputed_cities in get_subsets(cities):
        # Calculate the total cost of laying cables between the Byteland and disputed cities
        byteland_cost = get_cost(byteland_cities)
        # Calculate the total cost of laying cables between the Berland and disputed cities
        berland_cost = get_cost(disputed_cities)
        # Calculate the total cost of laying cables between the Byteland and Berland cities
        total_cost = byteland_cost + berland_cost
        # Update the minimum total cost if necessary
        min_cost = min(min_cost, total_cost)
    
    # Return the minimum total cost
    return min_cost

def get_subsets(cities):
    
    # Initialize an empty list to store the subsets
    subsets = []
    
    # Iterate over all possible combinations of cities
    for i in range(len(cities) + 1):
        # Iterate over all combinations of cities of size i
        for combination in itertools.combinations(cities, i):
            # Add the combination to the list of subsets
            subsets.append(list(combination))
    
    # Return the list of subsets
    return subsets

def get_cost(cities):
    
    # Initialize the total cost to zero
    cost = 0
    
    # Iterate over all pairs of cities
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            # Calculate the distance between the two cities
            distance = abs(cities[i] - cities[j])
            # Add the distance to the total cost
            cost += distance
    
    # Return the total cost
    return cost

def main():
    # Read the number of cities and their coordinates from stdin
    n = int(input())
    cities = []
    for i in range(n):
        x, c = input().split()
        cities.append(int(x))
    
    # Call the get_min_cost function to get the minimum total cost
    min_cost = get_min_cost(cities)
    
    # Print the minimum total cost to stdout
    print(min_cost)

if __name__ == '__main__':
    main()

