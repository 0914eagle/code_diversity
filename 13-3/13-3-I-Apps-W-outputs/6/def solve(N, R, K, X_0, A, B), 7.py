
def solve(N, R, K, X_0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Initialize the current bucket index to 0
    current_bucket = 0

    # Iterate through each rain drop
    for i in range(R):
        # Calculate the bucket index for the current rain drop
        bucket_index = (A * current_bucket + B) % N

        # Check if the current bucket is full
        if water_levels[bucket_index] == K:
            # If the current bucket is full, overflow the water to the left
            water_levels[bucket_index] = 0
            current_bucket = (current_bucket - 1) % N

        # Add the water level for the current rain drop to the current bucket
        water_levels[bucket_index] += 1

        # Move on to the next bucket
        current_bucket = (current_bucket + 1) % N

    # Check if the leftmost bucket overflowed
    if water_levels[0] > 0:
        return "OVERFLOW"

    # Calculate the output value
    a = 0
    for i in range(R):
        a = (53 * a + water_levels[i]) % 199933

    return a

