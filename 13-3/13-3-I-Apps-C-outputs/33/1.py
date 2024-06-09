
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
            continue

        # Check if the current bottle is not full and the total liters are less than the target
        if bottles[current_bottle - 1] < T - total_liters:
            # If it is not full and the total liters are less than the target, fill the current bottle
            moves.append(f"fill {current_bottle}")
            total_liters += bottles[current_bottle - 1]
        else:
            # If it is not full and the total liters are greater than the target, transfer the remaining liters to the target bottle
            moves.append(f"transfer {current_bottle} 0")
            total_liters += T - total_liters
            break

    # Return the moves
    return moves

def f2(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # Check if the current bottle is empty
        if bottles[current_bottle - 1] == 0:
            # If it is empty, move on to the next bottle
            current_bottle += 1
            continue

        # Check if the current bottle is not empty and the total liters are less than the target
        if bottles[current_bottle - 1] < T - total_liters:
            # If it is not empty and the total liters are less than the target, transfer the current bottle to the target bottle
            moves.append(f"transfer {current_bottle} 0")
            total_liters += bottles[current_bottle - 1]
        else:
            # If it is not empty and the total liters are greater than the target, discard the current bottle
            moves.append(f"discard {current_bottle}")
            total_liters += T - total_liters
            break

    # Return the moves
    return moves

if __name__ == '__main__':
    # Read the input
    N = int(input())
    bottles = list(map(int, input().split()))
    T = int(input())

    # Check if the total number of bottles is valid
    if N < 1 or N > 100:
        print("impossible")
        exit()

    # Check if the total volume of the bottles is valid
    if sum(bottles) < T or sum(bottles) > 1000:
        print("impossible")
        exit()

    # Check if the target volume is valid
    if T < 1 or T > 100:
        print("impossible")
        exit()

    # Call the functions to get the moves
    moves1 = f1(bottles, T)
    moves2 = f2(bottles, T)

    # Check if the moves are valid
    if len(moves1) > 1000 or len(moves2) > 1000:
        print("impossible")
        exit()

    # Print the moves
    print("\n".join(moves1))
    print("\n".join(moves2))

