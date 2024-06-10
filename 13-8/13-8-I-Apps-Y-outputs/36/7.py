
def get_time_pressed(times_pressed):
    # Initialize the stopwatch with 0 seconds
    time = 0
    
    # Iterate through the list of times the button was pressed
    for t in times_pressed:
        # If the stopwatch is currently stopped, start it and set the time to the current time
        if time == 0:
            time = t
        # If the stopwatch is currently running, check if the current time is less than the current time
        elif time < t:
            # Add the difference between the current time and the current press time to the stopwatch time
            time += t - time
        # If the stopwatch is currently running and the current time is greater than the current press time, the stopwatch has been reset
        else:
            time = 0
    
    # Return the stopwatch time
    return time

def main():
    # Read the number of times the button was pressed
    n = int(input())
    
    # Read the times the button was pressed
    times_pressed = []
    for i in range(n):
        times_pressed.append(int(input()))
    
    # Get the stopwatch time
    time = get_time_pressed(times_pressed)
    
    # Print the stopwatch time
    print(time)

if __name__ == '__main__':
    main()

