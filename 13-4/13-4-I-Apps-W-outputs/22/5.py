
def solve(H, N, A, B):
    # Initialize the minimum total Magic Points to be consumed
    min_points = 0
    # Loop through each spell
    for i in range(N):
        # Calculate the health after casting the spell
        health = H - A[i]
        # If the health is less than or equal to 0, break the loop
        if health <= 0:
            break
        # Calculate the total Magic Points consumed so far
        points = sum(B[:i+1])
        # Update the minimum total Magic Points if necessary
        min_points = min(min_points, points)
    # Return the minimum total Magic Points
    return min_points

