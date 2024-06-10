
def get_energy_cost(parts, ropes):
    # Initialize a dictionary to store the energy cost of each part
    energy_cost = {i: 0 for i in range(1, len(parts) + 1)}

    # Loop through each rope and update the energy cost of the connected parts
    for rope in ropes:
        x, y = rope
        energy_cost[x] += parts[x - 1]
        energy_cost[y] += parts[y - 1]

    return energy_cost

def get_minimum_energy_cost(parts, ropes):
    # Get the energy cost of each part
    energy_cost = get_energy_cost(parts, ropes)

    # Sort the parts based on their energy cost in descending order
    sorted_parts = sorted(energy_cost.items(), key=lambda x: x[1], reverse=True)

    # Initialize the minimum energy cost to 0
    min_energy_cost = 0

    # Loop through each part and add its energy cost to the minimum energy cost
    for part, energy in sorted_parts:
        min_energy_cost += energy

    return min_energy_cost

def main():
    # Read the number of parts and ropes
    num_parts, num_ropes = map(int, input().split())

    # Read the parts
    parts = list(map(int, input().split()))

    # Read the ropes
    ropes = []
    for _ in range(num_ropes):
        x, y = map(int, input().split())
        ropes.append((x, y))

    # Get the minimum energy cost to remove all parts
    min_energy_cost = get_minimum_energy_cost(parts, ropes)

    # Print the minimum energy cost
    print(min_energy_cost)

if __name__ == '__main__':
    main()

