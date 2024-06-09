
def f1(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # If the current bottle is full, discard it and move on to the next one
        if bottles[current_bottle - 1] == 0:
            moves.append(f"discard {current_bottle}")
            current_bottle += 1
            continue

        # If the current bottle is not full, fill it with dry ice from the ice cream container
        moves.append(f"fill {current_bottle}")
        total_liters += bottles[current_bottle - 1]

        # If the total liters are greater than the target, transfer the excess to the ice cream mix
        if total_liters > T:
            moves.append(f"transfer {current_bottle} 0")
            total_liters -= T

    return moves

def f2(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # If the current bottle is empty, move on to the next one
        if bottles[current_bottle - 1] == 0:
            current_bottle += 1
            continue

        # If the current bottle is not empty, transfer dry ice to the ice cream mix
        moves.append(f"transfer {current_bottle} 0")
        total_liters += bottles[current_bottle - 1]

        # If the total liters are greater than the target, discard the excess
        if total_liters > T:
            moves.append(f"discard {current_bottle}")
            total_liters -= T

    return moves

if __name__ == '__main__':
    num_bottles = int(input())
    bottles = list(map(int, input().split()))
    T = int(input())

    moves = f1(bottles, T)
    if len(moves) > 100000:
        moves = f2(bottles, T)

    for move in moves:
        print(move)

