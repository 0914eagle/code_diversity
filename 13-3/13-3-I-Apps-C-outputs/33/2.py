
def f1(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # Check if the current bottle is full
        if bottles[current_bottle - 1] == 0:
            # If it is full, discard it and move on to the next bottle
            moves.append(f"discard {current_bottle}")
            current_bottle += 1
        else:
            # If it is not full, fill it with dry ice from the ice cream container
            moves.append(f"fill {current_bottle}")
            total_liters += bottles[current_bottle - 1]

        # Check if the current bottle is the target bottle
        if current_bottle == 0:
            # If it is the target bottle, transfer the dry ice to the ice cream mix
            moves.append(f"transfer {current_bottle} 0")
            total_liters -= bottles[current_bottle - 1]
            current_bottle += 1

    # Return the moves
    return moves

def f2(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # Check if the current bottle is full
        if bottles[current_bottle - 1] == 0:
            # If it is full, discard it and move on to the next bottle
            moves.append(f"discard {current_bottle}")
            current_bottle += 1
        else:
            # If it is not full, fill it with dry ice from the ice cream container
            moves.append(f"fill {current_bottle}")
            total_liters += bottles[current_bottle - 1]

        # Check if the current bottle is the target bottle
        if current_bottle == 0:
            # If it is the target bottle, transfer the dry ice to the ice cream mix
            moves.append(f"transfer {current_bottle} 0")
            total_liters -= bottles[current_bottle - 1]
            current_bottle += 1

    # Return the moves
    return moves

if __name__ == '__main__':
    bottles = [7, 8]
    T = 10
    moves = f1(bottles, T)
    print(*moves, sep='\n')

