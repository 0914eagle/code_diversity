
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is within the range of the torpedo
        if ship[0] <= n and ship[1] >= -n:
            # Check if the ship is on the same line as the torpedo
            if ship[0] == ship[1]:
                # If the ship is on the same line as the torpedo, it cannot be avoided
                return "impossible"
            # Check if the ship is above or below the torpedo
            elif ship[2] < 0 or ship[2] > n:
                # If the ship is above or below the torpedo, it cannot be avoided
                return "impossible"
            # Check if the ship is to the left or right of the torpedo
            elif ship[0] < 0 and ship[1] > 0:
                # If the ship is to the left of the torpedo, turn left
                instructions.append("-")
            elif ship[0] > 0 and ship[1] < 0:
                # If the ship is to the right of the torpedo, turn right
                instructions.append("+")
            else:
                # If the ship is on the same line as the torpedo, it cannot be avoided
                return "impossible"

    # If all ships can be avoided, return the instructions
    return "".join(instructions)

