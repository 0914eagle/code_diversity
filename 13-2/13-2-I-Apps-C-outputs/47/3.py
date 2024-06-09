
def solve(n, cans):
    # Initialize a list to store the number of cans that will explode
    num_exploding_cans = [0] * n

    # Loop through each can
    for i in range(n):
        # Get the location and blast radius of the current can
        x, r = cans[i]

        # Loop through each can after the current can
        for j in range(i+1, n):
            # Get the location of the next can
            y = cans[j][0]

            # Check if the next can is in the blast radius of the current can
            if x + r >= y >= x - r:
                # If it is, mark it as exploding
                num_exploding_cans[j] += 1

    return num_exploding_cans

