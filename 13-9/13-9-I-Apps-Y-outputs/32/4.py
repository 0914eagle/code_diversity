
def get_minimum_stones(stones):
    # Initialize the count of black and white stones
    black_stones = 0
    white_stones = 0
    
    # Iterate through the string of stones
    for stone in stones:
        if stone == "B":
            black_stones += 1
        else:
            white_stones += 1
    
    # Return the minimum number of stones needed to achieve Jiro's purpose
    return min(black_stones, white_stones)

def main():
    # Read a single line of input from stdin and convert it to an integer
    stones = input().strip()
    
    # Call the get_minimum_stones function and print the result
    print(get_minimum_stones(stones))

if __name__ == '__main__':
    main()

