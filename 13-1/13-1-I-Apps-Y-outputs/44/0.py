
def is_balanced(s):
    # Initialize a counter for black and white stones
    black_count = 0
    white_count = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # Check if the current stone is black or white
        if s[i] == "B":
            black_count += 1
        else:
            white_count += 1
        
        # If the difference between black and white stones is greater than 1, return False
        if abs(black_count - white_count) > 1:
            return False
    
    # If the difference is 1, return True
    return True

