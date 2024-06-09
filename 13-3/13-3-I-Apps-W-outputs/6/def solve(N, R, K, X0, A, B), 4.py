
def solve(N, R, K, X0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Iterate through each rain drop and update the water levels of the buckets
    for i in range(R):
        # Calculate the bucket number for the current rain drop
        bucket_num = (A * X0 + B) % N

        # If the bucket is full, overflow the water to the left
        if water_levels[bucket_num] == K:
            while water_levels[bucket_num] == K:
                bucket_num = (bucket_num - 1) % N

        # Add the water level for the current rain drop to the current bucket
        water_levels[bucket_num] += 1

        # Update X0 for the next iteration
        X0 = (A * X0 + B) % N

    # Check if the leftmost bucket overflowed
    if water_levels[0] > K:
        return "OVERFLOW"

    # Calculate the final answer
    a = 0
    for i in range(R):
        a = (53 * a + water_levels[i]) % 199933

    return a

