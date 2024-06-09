
def get_button_presses(f, s, g, u, d):
    # Initialize the number of button presses to 0
    num_presses = 0

    # If the starting floor is greater than the goal floor, use the stairs
    if s > g:
        return "use the stairs"

    # If the starting floor is equal to the goal floor, no button presses are needed
    if s == g:
        return num_presses

    # If the starting floor is less than the goal floor, calculate the number of button presses needed
    while s < g:
        # If the difference between the starting floor and the goal floor is greater than the up button's range, use the up button as many times as possible
        if g - s > u:
            num_presses += 1
            s += u
        # If the difference between the starting floor and the goal floor is less than the up button's range, use the up button the remaining number of times
        else:
            num_presses += 1
            s = g

    return num_presses

