
def get_expected_value(n):
    # Initialize the probability of each board
    probabilities = [1 / 8] * 8

    # Loop through each board
    for i in range(n - 1):
        # Initialize the new probabilities
        new_probabilities = [0] * 8

        # Loop through each board
        for j in range(8):
            # Get the current probability
            probability = probabilities[j]

            # Get the number of black stones for the current board
            num_black_stones = get_num_black_stones(j)

            # Loop through the adjacent boards
            for k in range(j - 1, j + 2):
                # Check if the board is valid
                if 0 <= k < 8:
                    # Get the number of black stones for the adjacent board
                    num_adjacent_black_stones = get_num_black_stones(k)

                    # Update the probability
                    new_probabilities[k] += probability * (num_adjacent_black_stones - num_black_stones) / 2

        # Update the probabilities
        probabilities = new_probabilities

    # Return the expected value
    return sum(i * p for i, p in enumerate(probabilities)) % 998244353

def get_num_black_stones(board):
    # Get the number of black stones
    if board == 0:
        return 0
    elif board == 1:
        return 1
    elif board == 2:
        return 0
    elif board == 3:
        return 2
    elif board == 4:
        return 1
    elif board == 5:
        return 3
    elif board == 6:
        return 2
    elif board == 7:
        return 3

if __name__ == '__main__':
    n = int(input())
    print(*[get_expected_value(i + 1) for i in range(n)], sep='\n')

