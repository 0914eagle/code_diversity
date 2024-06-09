
import itertools

def get_combinations(switches, bulbs):
    # Initialize a list to store the combinations
    combinations = []

    # Iterate over each bulb
    for bulb in bulbs:
        # Get the switches connected to the bulb
        connected_switches = switches[bulb - 1]

        # Get the number of switches that should be on to light the bulb
        num_on = bulbs[bulb - 1]

        # Iterate over all possible combinations of switch states
        for combination in itertools.product([0, 1], repeat=len(connected_switches)):
            # Check if the combination lights the bulb
            if sum(combination[i - 1] for i in connected_switches) % 2 == num_on:
                combinations.append(combination)

    return combinations

def main():
    # Read the input
    num_switches, num_bulbs = map(int, input().split())
    switches = [list(map(int, input().split())) for _ in range(num_bulbs)]
    bulbs = list(map(int, input().split()))

    # Get the combinations
    combinations = get_combinations(switches, bulbs)

    # Print the number of combinations
    print(len(combinations))

if __name__ == "__main__":
    main()

