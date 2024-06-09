
def f1(s):
    # Initialize variables
    n = len(s)
    lights = [int(i) for i in s]
    time = 0
    button_presses = 0

    # Iterate through each timestep
    while any(lights):
        # Check if any lights are off
        if any(lights):
            # Press the first button
            button_presses += 1
            lights[button_presses % n] = 1 - lights[button_presses % n]

        # Update the time
        time += 1

    # Return the earliest time all lights are on
    return time

def f2(s):
    # Initialize variables
    n = len(s)
    lights = [int(i) for i in s]
    time = 0
    button_presses = 0

    # Iterate through each timestep
    while any(lights):
        # Check if any lights are off
        if any(lights):
            # Press the first button
            button_presses += 1
            lights[button_presses % n] = 1 - lights[button_presses % n]

            # Update the time
            time += 1

    # Return the earliest time all lights are on
    return time

if __name__ == '__main__':
    s = input()
    print(f1(s))
    print(f2(s))

