
def solve(N, A, B, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    
    # Initialize the number of explosions needed to vanish all monsters
    explosions_needed = 0
    
    # Loop through the healths and cause explosions until all monsters are vanished
    for i in range(N):
        # Check if the current monster has health greater than 0
        if healths[i] > 0:
            # Calculate the damage to the current monster and its neighbors
            damage = A + B * (N - i - 1)
            
            # Update the healths of the current monster and its neighbors
            healths[i] -= damage
            for j in range(i+1, N):
                healths[j] -= B
            
            # Increment the number of explosions needed
            explosions_needed += 1
    
    return explosions_needed

