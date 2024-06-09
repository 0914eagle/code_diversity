
def solve(N, R, K, X_0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Iterate through each rain drop and calculate the bucket it falls into
    for i in range(R):
        bucket = (A * X_0 + B) % N
        X_0 = bucket

        # If the bucket is full, overflow the water to the left
        if water_levels[bucket] == K:
            while water_levels[bucket] == K:
                bucket = (bucket - 1) % N
            water_levels[bucket] += 1
        else:
            water_levels[bucket] += 1

    # Check if the leftmost bucket overflowed
    if water_levels[0] > K:
        return "OVERFLOW"

    # Calculate the output value
    a = 0
    for i in range(R):
        a = (53 * a + water_levels[i]) % 199933

    return a

