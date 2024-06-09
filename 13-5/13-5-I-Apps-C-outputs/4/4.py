
def f1(S):
    # Initialize variables
    n = len(S)
    lights = [int(s) for s in S]
    time = 0
    pressed = [False] * n

    # Iterate through time steps
    while not all(lights):
        # Check if any button should be pressed
        for i in range(n):
            if not pressed[i] and lights[i]:
                pressed[i] = True
                for j in range(i, n):
                    lights[j] = 1 - lights[j]

        # Increment time step
        time += 1

    return time

def f2(S):
    # Initialize variables
    n = len(S)
    lights = [int(s) for s in S]
    time = 0
    pressed = [False] * n

    # Iterate through time steps
    while not all(lights):
        # Check if any button should be pressed
        for i in range(n):
            if not pressed[i] and lights[i]:
                pressed[i] = True
                for j in range(i, n):
                    lights[j] = 1 - lights[j]

        # Increment time step
        time += 1

    return time

if __name__ == '__main__':
    S = input()
    print(f1(S))
    print(f2(S))

