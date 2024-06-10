
def get_energy(parts, ropes):
    # Initialize a dictionary to store the energy cost of each part
    energy_cost = {}
    for part in parts:
        energy_cost[part] = 0

    # Iterate over the ropes and update the energy cost of each part
    for rope in ropes:
        part1, part2 = rope
        energy_cost[part1] += parts[part2]
        energy_cost[part2] += parts[part1]

    # Return the sum of the energy cost of all parts
    return sum(energy_cost.values())

def get_min_energy(parts, ropes):
    # Initialize a list to store the parts that have not been removed
    unremoved_parts = list(parts.keys())

    # Initialize a variable to store the minimum total energy
    min_energy = 0

    # Iterate over the parts and remove them one by one
    while unremoved_parts:
        # Get the part with the minimum energy cost
        current_part = min(unremoved_parts, key=lambda x: energy_cost[x])

        # Remove the current part and update the energy cost of the remaining parts
        unremoved_parts.remove(current_part)
        min_energy += energy_cost[current_part]

        # Update the energy cost of the remaining parts
        for part in unremoved_parts:
            energy_cost[part] -= parts[current_part]

    # Return the minimum total energy
    return min_energy

def main():
    # Read the input data
    n, m = map(int, input().split())
    parts = {}
    for i in range(1, n+1):
        parts[i] = int(input())
    ropes = []
    for i in range(m):
        x, y = map(int, input().split())
        ropes.append((x, y))

    # Calculate the minimum total energy
    min_energy = get_min_energy(parts, ropes)

    # Print the minimum total energy
    print(min_energy)

if __name__ == '__main__':
    main()

