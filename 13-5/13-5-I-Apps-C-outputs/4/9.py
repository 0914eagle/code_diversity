
def f1(S):
    # Initialize variables
    n = len(S)
    lights = [int(i) for i in S]
    time = 0
    pressed = 0

    # Loop through each timestep
    while pressed < n:
        # Check if any light is off
        if any(lights):
            # Find the first off light and press its button
            for i in range(n):
                if not lights[i]:
                    lights[i] = 1
                    pressed += 1
                    break
        # Update the lights based on the propagation
        for i in range(n):
            if lights[i]:
                lights[(i+1)%n] = 1 - lights[(i+1)%n]
        time += 1

    return time

def f2(S):
    # Initialize variables
    n = len(S)
    lights = [int(i) for i in S]
    time = 0
    pressed = 0

    # Loop through each timestep
    while pressed < n:
        # Check if any light is off
        if any(lights):
            # Find the first off light and press its button
            for i in range(n):
                if not lights[i]:
                    lights[i] = 1
                    pressed += 1
                    break
        # Update the lights based on the propagation
        for i in range(n):
            if lights[i]:
                lights[(i+1)%n] = 1 - lights[(i+1)%n]
        time += 1

    return time

if __name__ == '__main__':
    S = input()
    print(f1(S))
    print(f2(S))

