
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
            # Add the ship to the list of ships that need to be avoided
            instructions.append(ship)

    # If there are no ships to avoid, return "impossible"
    if not instructions:
        return "impossible"

    # Sort the list of ships to avoid by their x-coordinate
    instructions.sort(key=lambda x: x[0])

    # Initialize a list to store the final instructions
    final_instructions = []

    # Loop through each ship to avoid and add the appropriate instruction
    for ship in instructions:
        # Check if the ship is already outside the range of the torpedo
        if ship[0] > n or ship[1] < -n:
            continue

        # Add the appropriate instruction to avoid the ship
        if ship[0] == ship[1]:
            final_instructions.append("0")
        elif ship[0] < ship[1]:
            final_instructions.append("-")
        else:
            final_instructions.append("+")

    # Return the final instructions
    return "".join(final_instructions)

