
def solve(N, R, K, X_0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Iterate through each rain drop
    for i in range(R):
        # Calculate the bucket number of the current rain drop
        bucket_num = (A * X_0 + B) % N

        # If the bucket is full, overflow the water to the left
        if water_levels[bucket_num] == K:
            while water_levels[bucket_num] == K:
                bucket_num = (bucket_num - 1) % N

        # Add the water level of the current rain drop to the current bucket
        water_levels[bucket_num] += 1

    # Check if the leftmost bucket is overflowing
    if water_levels[0] > K:
        return "OVERFLOW"

    # Calculate the output value
    a = 0
    for i in range(R):
        a = (53 * a + water_levels[i]) % 199933

    return a

