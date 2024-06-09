
def is_palindrome(r, g, b, w):
    # Calculate the total number of balls
    total_balls = r + g + b + w
    
    # Check if the total number of balls is even
    if total_balls % 2 != 0:
        return "No"
    
    # Calculate the number of red, green, and blue balls
    num_red = r // 2
    num_green = g // 2
    num_blue = b // 2
    
    # Check if the number of red, green, and blue balls is equal
    if num_red != num_green or num_green != num_blue:
        return "No"
    
    # Check if the number of white balls is equal to the number of red, green, and blue balls
    if w != num_red:
        return "No"
    
    # If all conditions are met, return "Yes"
    return "Yes"

