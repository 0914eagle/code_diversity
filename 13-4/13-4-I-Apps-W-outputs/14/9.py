
def get_painting_time(n_painters, painting_times):
    # Initialize a list to store the painting time for each picture
    painting_time = [0] * len(painting_times)
    
    # Loop through each painter
    for painter in range(n_painters):
        # Loop through each picture
        for picture in range(len(painting_times)):
            # Add the painting time for the current painter to the current picture
            painting_time[picture] += painting_times[picture][painter]
    
    return painting_time

def main():
    # Read the number of painters and pictures
    n_painters, n_pictures = map(int, input().split())
    
    # Read the painting times for each picture
    painting_times = []
    for _ in range(n_pictures):
        painting_times.append(list(map(int, input().split())))
    
    # Calculate the painting time for each picture
    painting_time = get_painting_time(n_painters, painting_times)
    
    # Print the painting time for each picture
    for time in painting_time:
        print(time)

if __name__ == '__main__':
    main()

