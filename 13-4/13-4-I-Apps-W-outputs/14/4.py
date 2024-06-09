
def get_painting_time(m, n, t):
    # Initialize a list to store the painting times
    painting_times = []
    
    # Loop through each picture
    for i in range(m):
        # Initialize a variable to store the current painting time
        current_time = 0
        
        # Loop through each painter
        for j in range(n):
            # Add the time the current painter needs to work on the current picture to the current painting time
            current_time += t[i][j]
        
        # Add the current painting time to the list of painting times
        painting_times.append(current_time)
    
    # Return the list of painting times
    return painting_times

def main():
    # Read the number of pictures and painters
    m, n = map(int, input().split())
    
    # Read the time each painter needs to work on each picture
    t = []
    for i in range(m):
        t.append(list(map(int, input().split())))
    
    # Calculate the painting times
    painting_times = get_painting_time(m, n, t)
    
    # Print the painting times
    for i in range(m):
        print(painting_times[i])

if __name__ == '__main__':
    main()

