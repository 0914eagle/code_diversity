
def solve(N, R, K, X_0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Iterate through each rain drop and calculate the bucket it falls into
    for i in range(R):
        bucket_index = (A * X_0 + B) % N
        if water_levels[bucket_index] == K:
            # If the bucket is full, overflow the water to the left
            for j in range(bucket_index, -1, -1):
                if water_levels[j] < K:
                    water_levels[j] += 1
                    break
        else:
            # If the bucket is not full, add the water to it
            water_levels[bucket_index] += 1

        # Update X_0 for the next iteration
        X_0 = (A * X_0 + B) % N

    # Check if the leftmost bucket overflowed
    if water_levels[0] > 0:
        return "OVERFLOW"

    # Calculate the output value
    a = 0
    for i in range(R):
        bucket_index = (A * X_0 + B) % N
        a = (53 * a + bucket_index) % 199933
        X_0 = (A * X_0 + B) % N

    return a
