
def get_energy_cost(parts, ropes):
    # Initialize a dictionary to store the energy cost of each part
    energy_cost = {}
    for part in parts:
        energy_cost[part] = 0

    # Loop through each rope and update the energy cost of the connected parts
    for rope in ropes:
        part1, part2 = rope
        energy_cost[part1] += parts[part2]
        energy_cost[part2] += parts[part1]

    # Return the minimum total energy cost
    return min(energy_cost.values())

def main():
    # Read the number of parts and ropes
    n, m = map(int, input().split())

    # Read the parts and ropes
    parts = list(map(int, input().split()))
    ropes = [list(map(int, input().split())) for _ in range(m)]

    # Find the minimum total energy cost
    min_energy = get_energy_cost(parts, ropes)

    # Print the minimum total energy cost
    print(min_energy)

if __name__ == '__main__':
    main()

