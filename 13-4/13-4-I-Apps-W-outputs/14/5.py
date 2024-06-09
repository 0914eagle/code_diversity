
def get_painter_times(n_painters, painter_times):
    # Initialize a list to store the times for each painter
    painter_times_list = []
    
    # Loop through each painter and their corresponding times
    for painter, times in enumerate(painter_times):
        # Calculate the total time for the current painter
        total_time = sum(times)
        
        # Add the total time to the list
        painter_times_list.append(total_time)
    
    # Return the list of painter times
    return painter_times_list

def get_picture_times(n_painters, painter_times_list):
    # Initialize a list to store the times for each picture
    picture_times_list = []
    
    # Loop through each painter and their corresponding times
    for painter, times in enumerate(painter_times_list):
        # Calculate the total time for the current painter
        total_time = sum(times)
        
        # Add the total time to the list
        picture_times_list.append(total_time)
    
    # Return the list of picture times
    return picture_times_list

def main():
    # Read the number of painters and pictures
    n_painters, n_pictures = map(int, input().split())
    
    # Read the painter times for each picture
    painter_times = []
    for _ in range(n_painters):
        painter_times.append(list(map(int, input().split())))
    
    # Calculate the painter times for each painter
    painter_times_list = get_painter_times(n_painters, painter_times)
    
    # Calculate the picture times for each picture
    picture_times_list = get_picture_times(n_painters, painter_times_list)
    
    # Print the picture times
    for time in picture_times_list:
        print(time)

if __name__ == '__main__':
    main()

