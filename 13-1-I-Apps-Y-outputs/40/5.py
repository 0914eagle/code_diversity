
def is_balanced(s):
    # Initialize a variable to keep track of the number of black stones
    num_black = 0
    # Iterate through the string
    for stone in s:
        # If the current stone is black, increment the number of black stones
        if stone == "B":
            num_black += 1
        # If the current stone is white and the number of black stones is odd, return false
        elif stone == "W" and num_black % 2 == 1:
            return False
        # If the current stone is white and the number of black stones is even, return true
        elif stone == "W" and num_black % 2 == 0:
            return True
    # If we reach the end of the string and the number of black stones is odd, return false
    if num_black % 2 == 1:
        return False
    # If we reach the end of the string and the number of black stones is even, return true
    return True

