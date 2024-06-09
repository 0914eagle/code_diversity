
def f1(S):
    # Initialize variables
    n = len(S)
    lights = [int(i) for i in S]
    time = 0
    button_presses = []

    # Loop until all lights are on
    while any(lights):
        # Check if any button presses are scheduled
        if button_presses:
            # If so, process the next button press
            button_press = button_presses.pop(0)
            lights[button_press - 1] = 1 - lights[button_press - 1]
            time += 1
        else:
            # If not, press the first button
            button_presses.append(1)
            lights[0] = 1 - lights[0]
            time += 1

        # Schedule button presses for the next timestep
        for i in range(1, n):
            if lights[i - 1] != lights[i]:
                button_presses.append(i + 1)

    return time

def f2(...):
    ...

if __name__ == '__main__':
    S = "1101"
    print(f1(S))

