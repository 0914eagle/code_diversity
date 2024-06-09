
def solve(player, num_cuboids, *cuboids):
    
    # Convert the dimensions of the cuboids to a list of tuples
    cuboids = [(x, y, z) for x, y, z in cuboids]

    # Initialize the winner as the player who starts the game
    winner = player

    # Loop through each cuboid
    for i in range(num_cuboids):
        # Get the current cuboid
        cuboid = cuboids[i]

        # If the cuboid is a single cuboid, remove it
        if len(cuboid) == 1:
            cuboids.remove(cuboid)
        # Otherwise, cut the cuboid into smaller cuboids
        else:
            # Get the dimensions of the cuboid
            x, y, z = cuboid

            # Cut the cuboid into smaller cuboids
            cuboids.extend([(x, y, z), (1, y, z), (x, 1, z), (x, y, 1), (1, 1, z), (x, 1, 1), (1, y, 1), (1, 1, 1)])

            # Remove the current cuboid
            cuboids.remove(cuboid)

    # Return the winner
    return winner

