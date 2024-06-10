
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

    # Return the total energy cost
    return sum(energy_cost.values())

def get_minimum_energy_cost(parts, ropes):
    # Initialize a list to store the parts that have not been removed
    remaining_parts = list(parts.keys())

    # Initialize a variable to store the minimum total energy cost
    minimum_energy_cost = 0

    # Iterate through the parts and remove the parts with the minimum energy cost
    while remaining_parts:
        # Find the part with the minimum energy cost
        minimum_energy_cost_part = min(remaining_parts, key=lambda part: energy_cost[part])

        # Remove the part with the minimum energy cost
        remaining_parts.remove(minimum_energy_cost_part)

        # Update the minimum total energy cost
        minimum_energy_cost += energy_cost[minimum_energy_cost_part]

    # Return the minimum total energy cost
    return minimum_energy_cost

def main():
    # Read the input data
    parts, ropes = read_input()

    # Calculate the energy cost of each part
    energy_cost = get_energy_cost(parts, ropes)

    # Calculate the minimum total energy cost
    minimum_energy_cost = get_minimum_energy_cost(parts, ropes)

    # Print the minimum total energy cost
    print(minimum_energy_cost)

def read_input():
    # Read the number of parts and ropes
    n, m = map(int, input().split())

    # Read the energy cost of each part
    parts = {}
    for i in range(1, n+1):
        parts[i] = int(input())

    # Read the ropes
    ropes = []
    for i in range(m):
        x, y = map(int, input().split())
        ropes.append((x, y))

    return parts, ropes

if __name__ == '__main__':
    main()

