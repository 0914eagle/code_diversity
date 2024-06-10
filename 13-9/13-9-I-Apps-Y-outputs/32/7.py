
def get_minimum_stones(stones):
    # Initialize variables
    black_stones = 0
    white_stones = 0
    
    # Count the number of black and white stones
    for stone in stones:
        if stone == "B":
            black_stones += 1
        else:
            white_stones += 1
    
    # Return the minimum number of stones needed to achieve Jiro's purpose
    if black_stones == white_stones:
        return 0
    else:
        return 1

def main():
    # Read a string of stones from standard input
    stones = input()
    
    # Call the get_minimum_stones function and print the result
    print(get_minimum_stones(stones))

if __name__ == '__main__':
    main()

