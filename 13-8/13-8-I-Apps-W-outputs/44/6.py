
def get_energy_cost(parts, ropes):
    # Initialize a dictionary to store the energy cost of each part
    energy_cost = {i: 0 for i in range(1, len(parts) + 1)}
    
    # Loop through each rope and update the energy cost of the connected parts
    for rope in ropes:
        x, y = rope[0], rope[1]
        energy_cost[x] += parts[x - 1]
        energy_cost[y] += parts[y - 1]
    
    return energy_cost

def get_minimum_energy_cost(parts, ropes):
    # Get the energy cost of each part
    energy_cost = get_energy_cost(parts, ropes)
    
    # Initialize a list to store the minimum energy cost of removing each part
    min_energy_cost = [float('inf') for _ in range(len(parts))]
    
    # Loop through each part and find the minimum energy cost of removing it
    for part in range(len(parts)):
        for rope in ropes:
            x, y = rope[0], rope[1]
            if x == part + 1:
                min_energy_cost[part] = min(min_energy_cost[part], energy_cost[y])
            elif y == part + 1:
                min_energy_cost[part] = min(min_energy_cost[part], energy_cost[x])
    
    # Return the sum of the minimum energy cost of removing all parts
    return sum(min_energy_cost)

def main():
    parts = list(map(int, input().split()))
    ropes = []
    for _ in range(int(input())):
        ropes.append(list(map(int, input().split())))
    print(get_minimum_energy_cost(parts, ropes))

if __name__ == '__main__':
    main()

