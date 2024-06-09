
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
                # Increment the number of cans that will explode if the current can is shot
                num_exploding_cans[i] += 1

    return num_exploding_cans

