
def f1(D, S):
    # Initialize an empty list to store the y-coordinates of the disintegrating droplets
    disintegrating_droplets = []
    
    # Iterate through each droplet
    for i in range(D):
        # Initialize a variable to store the y-coordinate of the current droplet
        current_droplet_y = None
        
        # Iterate through each sensor
        for j in range(S):
            # Check if the current droplet is within the range of the current sensor
            if x1 <= x <= x2 and y1 <= y <= y2:
                # If the current droplet is within the range of the current sensor, store its y-coordinate
                current_droplet_y = y
                break
        
        # If the current droplet did not disintegrate, store 0
        if current_droplet_y is None:
            disintegrating_droplets.append(0)
        # Otherwise, store the y-coordinate of the disintegrating droplet
        else:
            disintegrating_droplets.append(current_droplet_y)
    
    # Return the list of y-coordinates of the disintegrating droplets
    return disintegrating_droplets

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    D, S = map(int, input().split())
    droplets = []
    for i in range(D):
        x, y = map(int, input().split())
        droplets.append((x, y))
    sensors = []
    for i in range(S):
        x1, x2, y = map(int, input().split())
        sensors.append((x1, x2, y))
    disintegrating_droplets = f1(D, S, droplets, sensors)
    for y in disintegrating_droplets:
        print(y)

