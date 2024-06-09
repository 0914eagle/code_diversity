
def f1(L, n):
    # Initialize a list to store the points and directions
    points = []
    
    # Iterate through the input points and directions
    for i in range(n):
        # Split the input into the point and direction
        point, direction = input().split()
        
        # Convert the point to an integer and add it to the list
        points.append(int(point))
    
    # Sort the points in ascending order
    points.sort()
    
    # Initialize a variable to store the current position of the wire
    current_position = 0
    
    # Iterate through the points and directions
    for i in range(n):
        # Get the current point and direction
        point, direction = points[i]
        
        # Check if the current position is equal to the current point
        if current_position == point:
            # If the direction is clockwise, move the current position to the right
            if direction == "C":
                current_position += 1
            # If the direction is counterclockwise, move the current position to the left
            else:
                current_position -= 1
        
        # Check if the current position is greater than the current point
        elif current_position > point:
            # If the direction is clockwise, move the current position to the left
            if direction == "C":
                current_position -= 1
            # If the direction is counterclockwise, move the current position to the right
            else:
                current_position += 1
        
        # Check if the current position is less than the current point
        elif current_position < point:
            # If the direction is clockwise, move the current position to the right
            if direction == "C":
                current_position += 1
            # If the direction is counterclockwise, move the current position to the left
            else:
                current_position -= 1
    
    # Check if the current position is equal to the starting position
    if current_position == 0:
        return "SAFE"
    else:
        return "GHOST"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    L, n = map(int, input().split())
    print(f1(L, n))

