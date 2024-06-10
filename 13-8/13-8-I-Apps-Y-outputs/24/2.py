
def is_easily_playable(s):
    # Initialize a variable to keep track of the current position
    current_position = 1
    
    # Iterate through the string
    for char in s:
        # Check if the current position is odd
        if current_position % 2 == 1:
            # If the current position is odd, the character must be R, U, or D
            if char not in "RUD":
                return False
        # Check if the current position is even
        else:
            # If the current position is even, the character must be L, U, or D
            if char not in "LUD":
                return False
        # Increment the current position
        current_position += 1
    
    # If all characters are valid, return True
    return True

def main():
    s = input()
    if is_easily_playable(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

