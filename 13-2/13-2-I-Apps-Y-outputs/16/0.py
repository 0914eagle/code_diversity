
def get_largest_box_volume(n, V):
    # Initialize an empty list to store the volumes of the boxes
    volumes = []
    
    # Iterate through the input n times
    for i in range(n):
        # Read a line of input from stdin and split it into tokens
        l, w, h = map(int, input().split())
        
        # Calculate the volume of the current box
        volume = l * w * h
        
        # Add the volume to the list of volumes
        volumes.append(volume)
    
    # Find the largest volume in the list
    largest_volume = max(volumes)
    
    # Return the difference between the largest volume and V
    return largest_volume - V
    
if __name__ == '__main__':
    n, V = map(int, input().split())
    print(get_largest_box_volume(n, V))

