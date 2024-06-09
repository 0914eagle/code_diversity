
def get_painter_time(painter_data):
    # Initialize a dictionary to store the painter's work time
    painter_time = {}
    
    # Iterate over the painter data
    for painter, time in enumerate(painter_data):
        # If the painter is not in the dictionary, add them with the given time
        if painter not in painter_time:
            painter_time[painter] = time
        # Otherwise, add the given time to the current time
        else:
            painter_time[painter] += time
    
    # Return the painter's work time
    return painter_time

def get_picture_time(painter_time, n_painters):
    # Initialize a list to store the picture's ready time
    picture_time = []
    
    # Iterate over the painters
    for painter in range(n_painters):
        # If the painter is not in the dictionary, skip them
        if painter not in painter_time:
            continue
        # Otherwise, add the painter's work time to the list
        picture_time.append(painter_time[painter])
    
    # Return the picture's ready time
    return picture_time

def main():
    # Read the number of pictures and painters
    m, n = map(int, input().split())
    
    # Read the painter data
    painter_data = [list(map(int, input().split())) for _ in range(m)]
    
    # Get the painter's work time
    painter_time = get_painter_time(painter_data)
    
    # Get the picture's ready time
    picture_time = get_picture_time(painter_time, n)
    
    # Print the picture's ready time
    print(*picture_time, sep='\n')

if __name__ == '__main__':
    main()

