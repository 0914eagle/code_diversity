
def f1(n, S):
    # Initialize variables
    lights = [int(i) for i in S]
    button_presses = []
    time = 0

    # Loop until all lights are on
    while not all(lights):
        # Check if any button presses are scheduled for the current time step
        if time in button_presses:
            # Cancel out button presses that will toggle the same light as an earlier button press
            button_presses = [b for b in button_presses if b != time]

        # Process button presses for the current time step
        for b in button_presses:
            # Toggle the state of the light at the position indicated by the button press
            lights[b] = 1 - lights[b]

        # Schedule button presses for the next time step
        button_presses += [b + n for b in range(len(lights)) if lights[b] == 0]

        # Increment time
        time += 1

    # Return the earliest time at which all lights are on
    return time

def f2(n, S):
    # Initialize variables
    lights = [int(i) for i in S]
    button_presses = []
    time = 0

    # Loop until all lights are on
    while not all(lights):
        # Check if any button presses are scheduled for the current time step
        if time in button_presses:
            # Cancel out button presses that will toggle the same light as an earlier button press
            button_presses = [b for b in button_presses if b != time]

        # Process button presses for the current time step
        for b in button_presses:
            # Toggle the state of the light at the position indicated by the button press
            lights[b] = 1 - lights[b]

            # Schedule button presses for the next time step
            button_presses += [b + n for b in range(len(lights)) if lights[b] == 0]

        # Increment time
        time += 1

    # Return the earliest time at which all lights are on
    return time

if __name__ == '__main__':
    n = int(input())
    S = input()
    print(f1(n, S))
    print(f2(n, S))

