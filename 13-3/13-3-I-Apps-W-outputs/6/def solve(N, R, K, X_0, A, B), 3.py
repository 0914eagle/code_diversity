
def solve(N, R, K, X_0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Iterate through each rain drop and calculate which bucket it falls into
    for i in range(R):
        # Calculate the current bucket number using the given sequence
        current_bucket = (A * X_0 + B) % N

        # If the current bucket is full, overflow the water to the left
        if water_levels[current_bucket] == K:
            while water_levels[current_bucket] == K:
                current_bucket = (current_bucket - 1) % N

        # Add the water to the current bucket
        water_levels[current_bucket] += 1

        # Update the X_0 value for the next iteration
        X_0 = current_bucket

    # Check if the leftmost bucket overflowed
    if water_levels[0] > K:
        return "OVERFLOW"

    # Calculate the final answer
    a = 0
    for i in range(R):
        a = (53 * a + water_levels[i]) % 199933

    return a

