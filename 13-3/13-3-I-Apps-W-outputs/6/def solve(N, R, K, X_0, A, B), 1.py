
def solve(N, R, K, X_0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Initialize a variable to keep track of the current bucket index
    current_bucket = 0

    # Iterate through each rain drop
    for i in range(R):
        # Calculate the index of the bucket that the rain drop will fall into
        bucket_index = (A * current_bucket + B) % N

        # Check if the bucket is full
        if water_levels[bucket_index] == K:
            # If the bucket is full, overflow the water to the left
            water_levels[bucket_index] = 0
            current_bucket = (current_bucket - 1) % N

        # Add the water level of the current bucket
        water_levels[bucket_index] += 1

        # Move on to the next bucket
        current_bucket = (current_bucket + 1) % N

    # Check if the leftmost bucket overflowed
    if water_levels[0] > 0:
        return "OVERFLOW"

    # Calculate the final answer
    a = 0
    for i in range(R):
        a = (53 * a + (X_0 + i) % N) % 199933

    return a

