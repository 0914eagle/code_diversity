
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is within the range of the torpedo
        if ship[0] <= n and ship[1] >= -n:
            # Check if the ship is already avoided
            if instructions[abs(ship[0])] == "0":
                continue
            # Check if the ship can be avoided by turning left or right
            if ship[0] > 0:
                instructions[abs(ship[0])] = "-"
            else:
                instructions[abs(ship[0])] = "+"

    # Check if all the ships are avoided
    if "0" not in instructions:
        return "impossible"

    # Return the instructions
    return "".join(instructions)

