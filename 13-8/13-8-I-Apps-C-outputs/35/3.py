
def solve(n, s):
    # Initialize the number of returnable rooms to 0
    returnable_rooms = 0
    
    # Iterate through each conveyor belt
    for i in range(n):
        # If the conveyor belt is off, increment the number of returnable rooms
        if s[i] == "-":
            returnable_rooms += 1
        # If the conveyor belt is clockwise, decrement the number of returnable rooms
        elif s[i] == ">":
            returnable_rooms -= 1
    
    # Return the number of returnable rooms
    return returnable_rooms

