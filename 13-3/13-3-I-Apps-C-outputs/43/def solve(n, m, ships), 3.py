
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is already outside the range of the torpedo
        if ship[0] > n or ship[1] < -n:
            continue

        # Check if the ship is within the range of the torpedo
        if -n <= ship[0] <= n and -n <= ship[1] <= n:
            # Calculate the distance between the ship and the torpedo
            distance = abs(ship[0] - ship[1])

            # Check if the ship can be avoided by turning the torpedo
            if distance <= n:
                # Add the instruction to turn the torpedo
                instructions.append("+" if ship[0] > ship[1] else "-")
            else:
                # The ship cannot be avoided, return "impossible"
                return "impossible"

    # If all the ships can be avoided, return the instructions
    return "".join(instructions)

