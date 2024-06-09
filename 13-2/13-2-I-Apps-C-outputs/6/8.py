
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is already passed by the torpedo
        if ship[0] < 0 and ship[1] < 0:
            continue

        # Check if the ship is already hit by the torpedo
        if ship[0] > n and ship[1] > n:
            continue

        # Check if the ship is in the same row as the torpedo
        if ship[2] == 0:
            # If the ship is in the same row as the torpedo, it cannot be avoided
            return "impossible"

        # Check if the ship is in the same column as the torpedo
        if ship[0] == ship[1]:
            # If the ship is in the same column as the torpedo, it cannot be avoided
            return "impossible"

        # Check if the ship is in the same diagonal as the torpedo
        if abs(ship[0] - ship[1]) == abs(ship[2]):
            # If the ship is in the same diagonal as the torpedo, it cannot be avoided
            return "impossible"

    # If all the ships can be avoided, return the instructions
    return instructions

