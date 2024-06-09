
def f1(S):
    # Initialize variables
    n = len(S)
    lights = [int(i) for i in S]
    time = 0
    propagation = 0

    # Loop through each light and check if it is on
    for i in range(n):
        # If the light is on, check if it will be turned off by propagation
        if lights[i] == 1:
            # If the light will be turned off by propagation, update the propagation variable
            if i + propagation < n and lights[i + propagation] == 0:
                propagation += 1
        # If the light is off, check if it will be turned on by propagation
        else:
            # If the light will be turned on by propagation, update the propagation variable
            if i + propagation < n and lights[i + propagation] == 1:
                propagation -= 1

    # Return the earliest time all lights are on
    return time + propagation

def f2(...):
    # Function to handle input and output
    ...

if __name__ == '__main__':
    f2(...)

