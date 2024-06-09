
def solve(N, L, positions):
    # Calculate the maximum speed such that no two pieces of luggage are within 1 meter of each other
    max_speed = (L - 1) / N

    # Check if an optimal speed exists
    if max_speed < 0.1:
        return "no fika"

    # Return the maximum speed
    return max_speed

