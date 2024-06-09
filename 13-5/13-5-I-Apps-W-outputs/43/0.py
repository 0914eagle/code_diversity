
def get_min_operations(stones):
    # Initialize variables
    num_red_stones = 0
    num_white_stones = 0
    num_operations = 0

    # Loop through the stones and count the number of red and white stones
    for stone in stones:
        if stone == "R":
            num_red_stones += 1
        else:
            num_white_stones += 1

    # If there are no white stones, return 0
    if num_white_stones == 0:
        return 0

    # If there is only one white stone, return 1
    if num_white_stones == 1:
        return 1

    # If there are two or more white stones, return the minimum number of operations needed to move all the white stones to the end of the row
    return num_white_stones + num_red_stones - 1

def main():
    num_stones = int(input())
    stones = input()
    print(get_min_operations(stones))

if __name__ == '__main__':
    main()

