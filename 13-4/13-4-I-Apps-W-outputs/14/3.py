
def get_painter_times(n_painters, painter_times):
    # Initialize a list to store the times for each painter
    painter_times_list = []
    
    # Loop through each painter and their corresponding times
    for painter, times in enumerate(painter_times):
        # Calculate the total time for the painter to complete all pictures
        total_time = sum(times)
        
        # Add the total time to the list
        painter_times_list.append(total_time)
    
    # Return the list of painter times
    return painter_times_list

def get_picture_times(n_painters, painter_times_list):
    # Initialize a list to store the times for each picture
    picture_times_list = []
    
    # Loop through each picture and calculate the time it takes to complete
    for picture in range(n_painters):
        # Calculate the time it takes for the picture to be completed
        picture_time = sum(painter_times_list[picture:])
        
        # Add the time to the list
        picture_times_list.append(picture_time)
    
    # Return the list of picture times
    return picture_times_list

def main():
    # Read the number of painters and pictures
    n_painters, n_pictures = map(int, input().split())
    
    # Read the times for each painter
    painter_times = [list(map(int, input().split())) for _ in range(n_painters)]
    
    # Get the times for each painter
    painter_times_list = get_painter_times(n_painters, painter_times)
    
    # Get the times for each picture
    picture_times_list = get_picture_times(n_painters, painter_times_list)
    
    # Print the times for each picture
    for picture_time in picture_times_list:
        print(picture_time)

if __name__ == '__main__':
    main()

