
import itertools

def get_combinations(switches, bulbs):
    # Initialize a list to store the combinations
    combinations = []

    # Iterate over each bulb
    for bulb in bulbs:
        # Get the switches connected to the bulb
        connected_switches = bulb[1:]

        # Get the number of switches that should be on to light the bulb
        num_switches_on = bulb[0]

        # Iterate over each combination of switch states
        for combination in itertools.product([0, 1], repeat=len(connected_switches)):
            # Initialize a counter for the number of switches that are on
            num_switches_on_count = 0

            # Iterate over each switch in the combination
            for i, switch in enumerate(combination):
                # If the switch is on, increment the counter
                if switch == 1:
                    num_switches_on_count += 1

            # If the number of switches that are on is congruent to the number of switches that should be on modulo 2, add the combination to the list
            if num_switches_on_count % 2 == num_switches_on:
                combinations.append(combination)

    # Return the list of combinations
    return combinations

def main():
    # Read the input
    num_switches, num_bulbs = map(int, input().split())
    bulbs = []
    for _ in range(num_bulbs):
        bulbs.append(list(map(int, input().split())))

    # Get the combinations
    combinations = get_combinations(num_switches, bulbs)

    # Print the number of combinations
    print(len(combinations))

if __name__ == "__main__":
    main()

