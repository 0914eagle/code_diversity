
def f1(n, s):
    # Initialize variables
    lights = [int(i) for i in s]
    time = 0
    button_presses = []

    # Loop through each timestep
    while any(lights):
        # Check if any buttons need to be pressed
        for i in range(n):
            if lights[i] == 0 and i + 1 < n and lights[i + 1] == 1:
                button_presses.append(i)
                break

        # Update the lights
        for i in range(n):
            if lights[i] == 1 and i + 1 < n and lights[i + 1] == 0:
                lights[i] = 0
                lights[i + 1] = 1
            elif lights[i] == 0 and i + 1 < n and lights[i + 1] == 1:
                lights[i] = 1
                lights[i + 1] = 0

        # Update the time
        time += 1

    return time

def f2(n, s):
    # Initialize variables
    lights = [int(i) for i in s]
    time = 0
    button_presses = []

    # Loop through each timestep
    while any(lights):
        # Check if any buttons need to be pressed
        for i in range(n):
            if lights[i] == 0 and i + 1 < n and lights[i + 1] == 1:
                button_presses.append(i)
                break

        # Update the lights
        for i in range(n):
            if lights[i] == 1 and i + 1 < n and lights[i + 1] == 0:
                lights[i] = 0
                lights[i + 1] = 1
            elif lights[i] == 0 and i + 1 < n and lights[i + 1] == 1:
                lights[i] = 1
                lights[i + 1] = 0

        # Update the time
        time += 1

    return time

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

