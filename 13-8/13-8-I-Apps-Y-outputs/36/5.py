
def get_stopwatch_time(times):
    # Initialize the stopwatch time to 0
    stopwatch_time = 0
    
    # Iterate through the list of times
    for time in times:
        # If the current time is greater than the stopwatch time, update the stopwatch time
        if time > stopwatch_time:
            stopwatch_time = time
    
    # Return the stopwatch time
    return stopwatch_time

def main():
    # Read the number of times the button was pressed
    num_times = int(input())
    
    # Read the list of times the button was pressed
    times = []
    for i in range(num_times):
        times.append(int(input()))
    
    # Get the stopwatch time
    stopwatch_time = get_stopwatch_time(times)
    
    # Print the stopwatch time
    print(stopwatch_time)

if __name__ == '__main__':
    main()

