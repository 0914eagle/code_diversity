
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is already passed or will be passed by the time the torpedo runs out of fuel
        if ship[0] > n or ship[1] < 0:
            continue

        # Check if the ship is within the range of the torpedo
        if ship[0] <= n and ship[1] >= 0:
            # Add the ship to the list of ships that need to be avoided
            instructions.append(ship)

    # If there are no ships to avoid, return "impossible"
    if not instructions:
        return "impossible"

    # Sort the ships by their x-coordinate
    instructions.sort(key=lambda x: x[0])

    # Initialize the current x-coordinate of the torpedo
    current_x = 0

    # Loop through each ship and calculate the instructions for avoiding it
    for ship in instructions:
        # Calculate the distance between the torpedo and the ship
        distance = ship[0] - current_x

        # If the distance is odd, turn left
        if distance % 2 == 1:
            instructions.append("-")

        # If the distance is even, turn right
        else:
            instructions.append("+")

        # Update the current x-coordinate of the torpedo
        current_x = ship[1]

    # Return the instructions as a string
    return "".join(instructions)

