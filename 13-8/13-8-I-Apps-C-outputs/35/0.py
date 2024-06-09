
def solve(n, s):
    # Initialize the number of returnable rooms to 0
    returnable_rooms = 0
    
    # Iterate through each conveyor belt
    for i in range(n):
        # If the conveyor belt is off, all snakes can travel in either direction
        if s[i] == '-':
            returnable_rooms += 1
        # If the conveyor belt is clockwise, snakes can only travel from room i to (i+1) mod n
        elif s[i] == '>':
            returnable_rooms += 1
        # If the conveyor belt is anticlockwise, snakes can only travel from room (i+1) mod n to i
        elif s[i] == '<':
            returnable_rooms += 1
    
    # Return the number of returnable rooms
    return returnable_rooms

