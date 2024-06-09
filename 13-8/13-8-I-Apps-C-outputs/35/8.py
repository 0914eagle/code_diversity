
def solve(n, s):
    # Initialize the number of returnable rooms to 0
    returnable_rooms = 0
    
    # Iterate through each room
    for i in range(n):
        # If the current room is returnable
        if is_returnable(i, n, s):
            # Increment the number of returnable rooms
            returnable_rooms += 1
    
    # Return the number of returnable rooms
    return returnable_rooms

def is_returnable(i, n, s):
    # If the current room is the first room
    if i == 0:
        # If the conveyor belt leading to the next room is clockwise, return False
        if s[i] == '>':
            return False
        # Otherwise, return True
        else:
            return True
    # If the current room is the last room
    elif i == n - 1:
        # If the conveyor belt leading to the previous room is anticlockwise, return False
        if s[i] == '<':
            return False
        # Otherwise, return True
        else:
            return True
    # If the current room is in the middle
    else:
        # If the conveyor belt leading to the previous room is clockwise and the conveyor belt leading to the next room is anticlockwise, return False
        if s[i] == '>' and s[(i+1)%n] == '<':
            return False
        # Otherwise, return True
        else:
            return True

n = int(input())
s = input()
print(solve(n, s))

