
def get_min_stones(s):
    # Initialize variables
    black_stones = 0
    white_stones = 0
    min_stones = 0
    
    # Loop through the string
    for stone in s:
        if stone == "B":
            black_stones += 1
        else:
            white_stones += 1
    
    # Calculate the minimum number of stones needed
    if black_stones == 0 or white_stones == 0:
        min_stones = 1
    else:
        min_stones = abs(black_stones - white_stones)
    
    return min_stones

def main():
    s = input()
    print(get_min_stones(s))

if __name__ == '__main__':
    main()

