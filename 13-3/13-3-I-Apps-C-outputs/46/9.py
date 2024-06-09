
def f1(n, positions):
    # Initialize a dictionary to store the minimum number of rounds required to reach each position from each position
    dp = {position: [0] * n for position in positions}

    # Loop through each position
    for current_position in range(n):
        # Get the options available to Alice in the current position
        options = positions[current_position]

        # Loop through each option
        for option in options:
            # Get the positions available to Bob if Alice chooses this option
            next_positions = option.split()

            # Loop through each next position
            for next_position in next_positions:
                # If Alice can reach the next position from the current position, update the minimum number of rounds required
                if dp[current_position][next_position] == 0 or dp[current_position][next_position] > dp[current_position][option] + 1:
                    dp[current_position][next_position] = dp[current_position][option] + 1

    # Return the minimum number of rounds required to reach each position from each position
    return dp

def f2(n, positions):
    # Initialize a dictionary to store the minimum number of rounds required to reach each position from each position
    dp = {position: [0] * n for position in positions}

    # Loop through each position
    for current_position in range(n):
        # Get the options available to Alice in the current position
        options = positions[current_position]

        # Loop through each option
        for option in options:
            # Get the positions available to Bob if Alice chooses this option
            next_positions = option.split()

            # Loop through each next position
            for next_position in next_positions:
                # If Alice can reach the next position from the current position, update the minimum number of rounds required
                if dp[current_position][next_position] == 0 or dp[current_position][next_position] > dp[current_position][option] + 1:
                    dp[current_position][next_position] = dp[current_position][option] + 1

    # Return the minimum number of rounds required to reach each position from each position
    return dp

if __name__ == '__main__':
    n = int(input())
    positions = [input().split() for _ in range(n)]
    dp = f1(n, positions)
    for position in range(n):
        print(*dp[position])

