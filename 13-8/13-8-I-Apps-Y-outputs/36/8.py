
def get_stopwatch_time(button_presses):
    # Initialize the stopwatch time to 0 seconds
    stopwatch_time = 0
    
    # Iterate through the list of button presses
    for button_press in button_presses:
        # If the button is pressed when the stopwatch is off, start the stopwatch and set the time to the current time
        if stopwatch_time == 0:
            stopwatch_time = button_press
        # If the button is pressed when the stopwatch is on, add the time since the last button press to the current time
        else:
            stopwatch_time += button_press - stopwatch_time
    
    # Return the stopwatch time
    return stopwatch_time

def main():
    # Get the number of button presses
    num_button_presses = int(input())
    
    # Get the list of button press times
    button_press_times = []
    for _ in range(num_button_presses):
        button_press_times.append(int(input()))
    
    # Get the stopwatch time
    stopwatch_time = get_stopwatch_time(button_press_times)
    
    # Print the stopwatch time
    print(stopwatch_time)

if __name__ == '__main__':
    main()

