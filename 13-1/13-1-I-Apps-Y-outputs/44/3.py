
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
    # If the number of black stones is greater than the number of white stones, return 0
    elif black_stones > white_stones:
        return 0
    # If the number of white stones is greater than the number of black stones, return 0
    else:
        return 0

