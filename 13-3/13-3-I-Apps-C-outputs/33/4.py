
def f1(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # Fill the current bottle with dry ice
        moves.append(f"fill {current_bottle}")
        total_liters += bottles[current_bottle - 1]

        # Transfer dry ice from the current bottle to the target bottle (0)
        moves.append(f"transfer {current_bottle} 0")
        total_liters -= bottles[current_bottle - 1]

        # Discard the current bottle
        moves.append(f"discard {current_bottle}")

        # Increment the current bottle
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
        # Fill the current bottle with dry ice
        moves.append(f"fill {current_bottle}")
        total_liters += bottles[current_bottle - 1]

        # Transfer dry ice from the current bottle to the target bottle (0)
        moves.append(f"transfer {current_bottle} 0")
        total_liters -= bottles[current_bottle - 1]

        # Discard the current bottle
        moves.append(f"discard {current_bottle}")

        # Increment the current bottle
        current_bottle += 1

    # Return the moves
    return moves

if __name__ == '__main__':
    num_bottles = int(input())
    bottles = list(map(int, input().split()))
    T = int(input())

    moves = f1(bottles, T)
    print(*moves, sep='\n')

