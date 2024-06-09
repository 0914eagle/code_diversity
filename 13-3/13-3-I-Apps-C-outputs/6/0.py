
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
                # If the current droplet is within the range of the current sensor, set the current droplet y-coordinate to the sensor y-coordinate
                current_droplet_y = y
                break
        
        # If the current droplet did not disintegrate, set its y-coordinate to 0
        if current_droplet_y is None:
            current_droplet_y = 0
        
        # Add the current droplet y-coordinate to the list of disintegrating droplets
        disintegrating_droplets.append(current_droplet_y)
    
    # Return the list of disintegrating droplets
    return disintegrating_droplets

def f2(D, S):
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
                # If the current droplet is within the range of the current sensor, set the current droplet y-coordinate to the sensor y-coordinate
                current_droplet_y = y
                break
        
        # If the current droplet did not disintegrate, set its y-coordinate to 0
        if current_droplet_y is None:
            current_droplet_y = 0
        
        # Add the current droplet y-coordinate to the list of disintegrating droplets
        disintegrating_droplets.append(current_droplet_y)
    
    # Return the list of disintegrating droplets
    return disintegrating_droplets

if __name__ == '__main__':
    D, S = map(int, input().split())
    droplets = []
    sensors = []
    
    for i in range(D):
        x, y = map(int, input().split())
        droplets.append((x, y))
    
    for i in range(S):
        x1, x2, y = map(int, input().split())
        sensors.append((x1, x2, y))
    
    disintegrating_droplets = f1(D, S, droplets, sensors)
    print(*disintegrating_droplets, sep='\n')

