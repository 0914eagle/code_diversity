
def solve(N, trenches):
    # Initialize a list to store the guards' positions
    guards = [0] * N

    # Iterate through each trench
    for trench in trenches:
        # Get the coordinates of the trench's ends
        x1, y1, x2, y2 = trench

        # If the trench is horizontal or vertical
        if x1 == x2 or y1 == y2:
            # Get the coordinates of the other end
            if x1 == x2:
                x3, y3 = x1, y2
            else:
                x3, y3 = x2, y1

            # Iterate through the guards
            for i in range(N):
                # If the guard is not already placed on the trench
                if guards[i] == 0:
                    # Check if the guard is within the trench
                    if x3 >= guards[i] and x3 <= guards[i] + 1 and y3 >= guards[i] and y3 <= guards[i] + 1:
                        # Place the guard on the trench
                        guards[i] = x3
                        break

    # Return the number of guards placed on a single line
    return sum(guards)

