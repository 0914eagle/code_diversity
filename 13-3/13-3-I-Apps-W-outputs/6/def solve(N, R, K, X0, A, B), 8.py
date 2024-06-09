
def solve(N, R, K, X0, A, B):
    # Initialize an array to store the water levels of the buckets
    water_levels = [0] * N

    # Calculate the sequence of buckets for the rain drops
    buckets = [(A * X0 + B) % N]
    for i in range(1, R):
        buckets.append((A * buckets[i-1] + B) % N)

    # Check if the leftmost bucket overflows
    if water_levels[buckets[0]] + 1 > K:
        return "OVERFLOW"

    # Update the water levels of the buckets
    for i in range(R):
        water_levels[buckets[i]] += 1

    # Calculate the final answer
    a = 0
    for i in range(R):
        a = (53 * a + buckets[i]) % 199933

    return a

