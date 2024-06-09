
def is_balanced(s):
    # Initialize variables to keep track of the number of black and white stones
    black_stones = 0
    white_stones = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current stone is black, increment the black stone count
        if s[i] == "B":
            black_stones += 1
        # If the current stone is white, increment the white stone count
        elif s[i] == "W":
            white_stones += 1
    
    # If the number of black stones is equal to the number of white stones, return 1
    if black_stones == white_stones:
        return 1
    # If the number of black stones is one more than the number of white stones, return 1
    elif black_stones == white_stones + 1:
        return 1
    # If the number of white stones is one more than the number of black stones, return 1
    elif white_stones == black_stones + 1:
        return 1
    # Otherwise, return 0
    else:
        return 0

if __name__ == '__main__':
    s = input()
    print(is_balanced(s))

