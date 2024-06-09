
import itertools

def get_combinations(switches, bulbs):
    # Initialize a list to store the combinations
    combinations = []

    # Iterate over each bulb
    for bulb in bulbs:
        # Get the list of switches connected to the bulb
        switch_list = bulb[1:]

        # Get the number of switches that should be on for the bulb to be lit
        num_on = bulb[0]

        # Iterate over each combination of switch states
        for state in itertools.product([0, 1], repeat=len(switch_list)):
            # Check if the number of on switches is congruent to the required number
            if sum(state) % 2 == num_on:
                # Add the combination to the list of combinations
                combinations.append(state)

    # Return the list of combinations
    return combinations

def main():
    # Read the input
    num_switches, num_bulbs = map(int, input().split())
    bulbs = [list(map(int, input().split())) for _ in range(num_bulbs)]

    # Get the combinations of switch states that light all the bulbs
    combinations = get_combinations(num_switches, bulbs)

    # Print the number of combinations
    print(len(combinations))

if __name__ == "__main__":
    main()

