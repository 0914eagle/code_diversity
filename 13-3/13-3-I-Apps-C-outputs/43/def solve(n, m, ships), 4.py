
def solve(n, m, ships):
    # Initialize the solution string
    solution = ""

    # Loop through each ship
    for ship in ships:
        # Check if the ship is already hit
        if ship[0] == ship[1]:
            continue

        # Check if the ship is on the same y-coordinate as the torpedo
        if ship[2] != 0:
            continue

        # Check if the ship is within the range of the torpedo
        if abs(ship[0]) > n or abs(ship[1]) > n:
            continue

        # Check if the ship is on the same x-coordinate as the torpedo
        if ship[0] == 0 and ship[1] == 0:
            return "impossible"

        # Check if the ship is on the left side of the torpedo
        if ship[0] < 0 and ship[1] > 0:
            solution += "-"
        # Check if the ship is on the right side of the torpedo
        elif ship[0] > 0 and ship[1] < 0:
            solution += "+"
        # Check if the ship is on the same side of the torpedo
        else:
            solution += "0"

    return solution

