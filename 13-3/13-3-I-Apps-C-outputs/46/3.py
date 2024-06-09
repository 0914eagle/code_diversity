
def f1(n, positions):
    # Initialize a dictionary to store the minimum number of rounds required to reach each position from each position
    dp = {position: {position: 0 for position in positions} for position in positions}

    # Loop through each position and calculate the minimum number of rounds required to reach each position from that position
    for position in positions:
        for option in positions:
            if option != position:
                dp[position][option] = 1 + dp[option][position]

    # Return the dictionary
    return dp

def f2(n, positions, start_position, end_position):
    # Initialize a dictionary to store the minimum number of rounds required to reach each position from the start position
    dp = {position: float('inf') for position in positions}
    dp[start_position] = 0

    # Loop through each position and calculate the minimum number of rounds required to reach each position from the start position
    for i in range(n):
        for position in positions:
            for option in positions:
                if option != position and dp[position] != float('inf'):
                    dp[option] = min(dp[option], dp[position] + 1)

    # Return the minimum number of rounds required to reach the end position from the start position
    return dp[end_position]

if __name__ == '__main__':
    n = int(input())
    positions = input().split()
    start_position = input()
    end_position = input()
    dp = f1(n, positions)
    print(f2(n, positions, start_position, end_position))

