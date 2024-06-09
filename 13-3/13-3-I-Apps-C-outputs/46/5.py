
def f1(n, positions):
    # Initialize a dictionary to store the minimum number of rounds required to reach each position from each position
    dp = {position: [0] * n for position in positions}

    # Loop through each position
    for current_position in range(n):
        # Get the options available to Alice in the current position
        options = positions[current_position]

        # Loop through each option
        for option in options:
            # Get the next position that Bob can move to
            next_position = option[0]

            # If the next position is not the current position, update the minimum number of rounds required to reach the next position from the current position
            if next_position != current_position:
                dp[current_position][next_position] = 1 + dp[next_position][current_position]

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
            # Get the next position that Bob can move to
            next_position = option[0]

            # If the next position is not the current position, update the minimum number of rounds required to reach the next position from the current position
            if next_position != current_position:
                dp[current_position][next_position] = 1 + dp[next_position][current_position]

    # Return the minimum number of rounds required to reach each position from each position
    return dp

if __name__ == '__main__':
    n = int(input())
    positions = [input().split() for _ in range(n)]
    dp = f1(n, positions)
    for position in range(n):
        print(*dp[position])

