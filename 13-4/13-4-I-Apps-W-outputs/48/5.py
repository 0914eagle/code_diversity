
def get_winner(player_name, num_cuboids, *cuboid_sizes):
    
    # Initialize the winner as the starting player
    winner = player_name

    # Loop through each cuboid
    for i in range(num_cuboids):
        # Get the current cuboid size
        x, y, z = cuboid_sizes[i]

        # Check if the current player can make a move
        if winner == "RUBEN":
            # Ruben's move
            if x > 1:
                # Cut the cuboid along the x-axis
                winner = "ALBERT"
            elif y > 1:
                # Cut the cuboid along the y-axis
                winner = "ALBERT"
            elif z > 1:
                # Cut the cuboid along the z-axis
                winner = "ALBERT"
        else:
            # Albert's move
            if x > 1:
                # Cut the cuboid along the x-axis
                winner = "RUBEN"
            elif y > 1:
                # Cut the cuboid along the y-axis
                winner = "RUBEN"
            elif z > 1:
                # Cut the cuboid along the z-axis
                winner = "RUBEN"

    # Return the winner
    return winner

def main():
    
    # Get the input from the user
    player_name = input("Enter the name of the starting player: ")
    num_cuboids = int(input("Enter the number of cuboids: "))
    cuboid_sizes = []
    for i in range(num_cuboids):
        x, y, z = map(int, input("Enter the size of the cuboid: ").split())
        cuboid_sizes.append((x, y, z))

    # Get the winner
    winner = get_winner(player_name, num_cuboids, *cuboid_sizes)

    # Print the winner
    print(f"The winner is {winner}.")

if __name__ == '__main__':
    main()

