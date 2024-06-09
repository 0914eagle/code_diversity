
def f1(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # If the current bottle is full, move to the next bottle
        if bottles[current_bottle - 1] == 0:
            current_bottle += 1
            continue

        # Fill the current bottle from the ice cream container
        moves.append(f"fill {current_bottle}")
        bottles[current_bottle - 1] = 0
        total_liters += 1

        # If the current bottle is now full, move to the next bottle
        if bottles[current_bottle - 1] == 0:
            current_bottle += 1
            continue

        # Transfer dry ice from the current bottle to the target bottle (bottle 0)
        moves.append(f"transfer {current_bottle} 0")
        bottles[current_bottle - 1] -= 1
        total_liters += 1

    # If the total liters is not equal to T, it is not possible to add the correct amount of dry ice
    if total_liters != T:
        return "impossible"

    return " ".join(moves)

def f2(...):
    ...

if __name__ == '__main__':
    ...

