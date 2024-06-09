
def solve(N, a):
    # Initialize a set to store the indices of the buttons that are lightened up
    lightened_up = set()
    # Add the index of Button 1 to the set
    lightened_up.add(1)
    # Initialize a variable to store the minimum number of times we need to press buttons
    min_presses = 0
    # Loop through the indices of the buttons
    for i in range(2, N+1):
        # If the current button is lightened up, add its index to the set and increment the minimum number of presses
        if i in lightened_up:
            lightened_up.add(a[i-1])
            min_presses += 1
        # If the current button is not lightened up and its index is not in the set, add it to the set and increment the minimum number of presses
        elif i not in lightened_up:
            lightened_up.add(i)
            min_presses += 1
        # If the current button is not lightened up and its index is in the set, do nothing
        else:
            pass
    # If Button 2 is lightened up, return the minimum number of presses, otherwise return -1
    if 2 in lightened_up:
        return min_presses
    else:
        return -1

