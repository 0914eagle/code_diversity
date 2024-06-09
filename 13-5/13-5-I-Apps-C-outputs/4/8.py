
def f1(S):
    # Initialize variables
    n = len(S)
    lights = [int(s) for s in S]
    time = 0
    button_presses = []

    # Loop until all lights are on
    while not all(lights):
        # Check if any button presses are scheduled to occur at the current time
        if time in button_presses:
            # Cancel out the propagation of the button press
            button_presses.remove(time)
        else:
            # Press the first button that is not on
            for i in range(n):
                if not lights[i]:
                    button_presses.append(time + i + 1)
                    break

        # Update the lights based on the button presses
        for i in range(n):
            if time + i + 1 in button_presses:
                lights[i] = 1 - lights[i]

        # Increment the time
        time += 1

    # Return the earliest time all lights are on
    return time

def f2(S):
    # Initialize variables
    n = len(S)
    lights = [int(s) for s in S]
    time = 0
    button_presses = []

    # Loop until all lights are on
    while not all(lights):
        # Check if any button presses are scheduled to occur at the current time
        if time in button_presses:
            # Cancel out the propagation of the button press
            button_presses.remove(time)
        else:
            # Press the first button that is not on
            for i in range(n):
                if not lights[i]:
                    button_presses.append(time + i + 1)
                    break

        # Update the lights based on the button presses
        for i in range(n):
            if time + i + 1 in button_presses:
                lights[i] = 1 - lights[i]

        # Increment the time
        time += 1

    # Return the earliest time all lights are on
    return time

if __name__ == '__main__':
    S = "1101"
    print(f1(S))
    print(f2(S))

