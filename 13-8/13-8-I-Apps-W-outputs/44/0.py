
def get_energy_cost(parts, ropes):
    # Initialize a dictionary to store the energy cost of each part
    energy_cost = {}
    for part in parts:
        energy_cost[part] = 0
    
    # Iterate through the ropes and update the energy cost of each part
    for rope in ropes:
        part1, part2 = rope
        energy_cost[part1] += parts[part2]
        energy_cost[part2] += parts[part1]
    
    return energy_cost

def get_minimum_energy_cost(parts, ropes):
    # Get the energy cost of each part
    energy_cost = get_energy_cost(parts, ropes)
    
    # Initialize the minimum energy cost to 0
    min_energy_cost = 0
    
    # Iterate through the parts and update the minimum energy cost
    for part in parts:
        min_energy_cost += energy_cost[part]
    
    return min_energy_cost

def main():
    # Read the number of parts and ropes
    n, m = map(int, input().split())
    
    # Read the parts and ropes
    parts = list(map(int, input().split()))
    ropes = []
    for _ in range(m):
        rope = list(map(int, input().split()))
        ropes.append(rope)
    
    # Calculate the minimum energy cost
    min_energy_cost = get_minimum_energy_cost(parts, ropes)
    
    # Print the minimum energy cost
    print(min_energy_cost)

if __name__ == '__main__':
    main()

