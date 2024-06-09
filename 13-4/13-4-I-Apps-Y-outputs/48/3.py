
import itertools

def solve(switches, bulbs):
    # Initialize a list to store the number of combinations for each bulb
    combinations = [0] * len(bulbs)

    # Iterate over each bulb
    for i, bulb in enumerate(bulbs):
        # Get the list of switches connected to the bulb
        switch_list = switches[bulb[0]:bulb[1]+1]

        # Iterate over all possible combinations of switch states
        for state in itertools.product([0, 1], repeat=len(switch_list)):
            # Check if the current combination lights the bulb
            if sum(state) % 2 == bulb[2]:
                # Increment the number of combinations for the bulb
                combinations[i] += 1

    # Return the sum of the number of combinations for all bulbs
    return sum(combinations)

# Main
if __name__ == '__main__':
    # Read the input
    N, M = map(int, input().split())
    switches = [list(map(int, input().split())) for _ in range(M)]
    bulbs = [list(map(int, input().split())) for _ in range(M)]

    # Solve the problem
    result = solve(switches, bulbs)

    # Print the result
    print(result)

