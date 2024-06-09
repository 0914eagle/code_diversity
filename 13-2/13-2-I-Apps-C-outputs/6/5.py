
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

            # Check if the ship can be avoided by turning left or right
            if distance % 2 == 0:
                instructions.append("-")
            else:
                instructions.append("+")

    # If all ships can be avoided, return the instructions
    if len(instructions) == m:
        return "".join(instructions)

    # If not all ships can be avoided, return "impossible"
    return "impossible"

