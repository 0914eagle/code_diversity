
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
    # Initialize a list to store the parts that have been removed
    removed_parts = []

    # Iterate through the parts and remove the parts with the minimum energy cost
    while parts:
        # Find the part with the minimum energy cost that has not been removed
        minimum_energy_cost = float('inf')
        for part in parts:
            if part not in removed_parts and energy_cost[part] < minimum_energy_cost:
                minimum_energy_cost = energy_cost[part]
                part_to_remove = part

        # Remove the part with the minimum energy cost
        removed_parts.append(part_to_remove)
        parts.remove(part_to_remove)

    # Return the total energy cost
    return get_energy_cost(parts, ropes)

def main():
    parts = [10, 20, 30, 40]
    ropes = [(1, 4), (1, 2), (2, 3), (2, 4)]
    print(get_minimum_energy_cost(parts, ropes))

if __name__ == '__main__':
    main()

