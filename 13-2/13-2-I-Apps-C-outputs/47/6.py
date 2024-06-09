
def solve(n, cans):
    # Initialize a list to store the number of cans that will explode
    num_exploding_cans = [0] * n

    # Loop through each can
    for i in range(n):
        # Get the location and blast radius of the current can
        x, r = cans[i]

        # Loop through each can again
        for j in range(n):
            # If the current can is not the same as the current can and it is within the blast radius
            if i != j and abs(x - cans[j][0]) <= r:
                # Increment the number of cans that will explode
                num_exploding_cans[i] += 1

    return num_exploding_cans

