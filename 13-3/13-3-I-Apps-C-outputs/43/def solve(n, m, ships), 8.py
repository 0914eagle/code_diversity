
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is already out of range
        if ship[0] > n or ship[1] < -n:
            continue

        # Check if the ship is within range and can be avoided
        if ship[0] <= n and ship[1] >= -n:
            # Add the appropriate instruction to avoid the ship
            instructions.append("-" if ship[0] < 0 else "+" if ship[0] > 0 else "0")
        else:
            # The ship cannot be avoided, return "impossible"
            return "impossible"

    # If all ships can be avoided, return the instructions
    return "".join(instructions)

