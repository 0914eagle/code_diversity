
def get_minimum_stones(S):
    # Initialize the variables
    num_black_stones = 0
    num_white_stones = 0
    is_black_stone = True

    # Iterate through the string S
    for char in S:
        if char == "B":
            num_black_stones += 1
        else:
            num_white_stones += 1

    # Check if the board is already balanced
    if num_black_stones == num_white_stones:
        return 0

    # Check if Jiro needs to place more black stones or white stones
    if num_black_stones > num_white_stones:
        is_black_stone = False

    # Calculate the minimum number of stones needed to be placed
    min_stones = abs(num_black_stones - num_white_stones)

    # Return the minimum number of stones needed to be placed
    return min_stones

def main():
    S = input()
    print(get_minimum_stones(S))

if __name__ == '__main__':
    main()

