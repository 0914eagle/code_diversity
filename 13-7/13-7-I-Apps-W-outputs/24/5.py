
def solve(player, n, cuboids):
    # Initialize the winner as the player who starts the game
    winner = player
    
    # Loop through each cuboid
    for i in range(n):
        # Get the current cuboid
        x, y, z = cuboids[i]
        
        # Check if the cuboid is already removed
        if x == 0 or y == 0 or z == 0:
            continue
        
        # Check if the cuboid can be removed
        if x == 1 or y == 1 or z == 1:
            # Remove the cuboid
            x = 0
            y = 0
            z = 0
        else:
            # Cut the cuboid into smaller cuboids
            x //= 2
            y //= 2
            z //= 2
        
        # Check if the current player is Ruben
        if player == "RUBEN":
            # Change the player to Albert
            player = "ALBERT"
        else:
            # Change the player to Ruben
            player = "RUBEN"
    
    # Return the winner
    return winner

