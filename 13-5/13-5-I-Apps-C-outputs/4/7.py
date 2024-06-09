
def f1(S):
    # Initialize variables
    n = len(S)
    lights = [int(s) for s in S]
    time = 0
    pressed = [-1] * n

    # Loop until all lights are on
    while any(lights):
        # Find the first light that is off
        i = lights.index(0)

        # Press the button for that light
        pressed[i] = time

        # Toggle the state of the light and all subsequent lights
        for j in range(i, n):
            lights[j] = 1 - lights[j]

        # Increment the time
        time += 1

    # Return the earliest time all lights are on
    return time

def f2(S):
    # Initialize variables
    n = len(S)
    lights = [int(s) for s in S]
    time = 0
    pressed = [-1] * n

    # Loop until all lights are on
    while any(lights):
        # Find the first light that is off
        i = lights.index(0)

        # Press the button for that light
        pressed[i] = time

        # Toggle the state of the light and all subsequent lights
        for j in range(i, n):
            lights[j] = 1 - lights[j]

        # Increment the time
        time += 1

    # Return the earliest time all lights are on
    return time

if __name__ == '__main__':
    S = input()
    print(f1(S))

