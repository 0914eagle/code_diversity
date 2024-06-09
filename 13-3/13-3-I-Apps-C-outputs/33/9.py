
def f1(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # If the current bottle is full, discard it and move on to the next one
        if bottles[current_bottle - 1] == 100:
            moves.append(f"discard {current_bottle}")
            current_bottle += 1
            continue

        # If the current bottle is not full, fill it with dry ice from the ice cream container
        moves.append(f"fill {current_bottle}")
        total_liters += 100

        # If the current bottle is now full, transfer dry ice from it into the ice cream mix
        if bottles[current_bottle - 1] == 100:
            moves.append(f"transfer {current_bottle} 0")
            total_liters -= 100

    return moves

def f2(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # If the current bottle is empty, discard it and move on to the next one
        if bottles[current_bottle - 1] == 0:
            moves.append(f"discard {current_bottle}")
            current_bottle += 1
            continue

        # If the current bottle is not empty, transfer dry ice from it into the ice cream mix
        moves.append(f"transfer {current_bottle} 0")
        total_liters += 100

        # If the current bottle is now empty, fill it with dry ice from the ice cream container
        if bottles[current_bottle - 1] == 0:
            moves.append(f"fill {current_bottle}")
            total_liters -= 100

    return moves

if __name__ == '__main__':
    bottles = [7, 8]
    T = 10
    moves = f1(bottles, T)
    print(*moves, sep='\n')

