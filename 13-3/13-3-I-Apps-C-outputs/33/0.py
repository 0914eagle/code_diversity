
def f1(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # Check if the current bottle is full
        if bottles[current_bottle - 1] == 0:
            # If it is full, discard it and move to the next bottle
            moves.append(f"discard {current_bottle}")
            current_bottle += 1
        else:
            # If it is not full, fill it with dry ice from the ice cream container
            moves.append(f"fill {current_bottle}")
            total_liters += bottles[current_bottle - 1]

        # Check if the current bottle is the target bottle
        if current_bottle == 0:
            # If it is the target bottle, break the loop
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
            # If it is empty, move to the next bottle
            current_bottle += 1
        else:
            # If it is not empty, transfer dry ice from it into the target bottle
            moves.append(f"transfer {current_bottle} 0")
            total_liters += bottles[current_bottle - 1]

        # Check if the current bottle is the target bottle
        if current_bottle == 0:
            # If it is the target bottle, break the loop
            break

    # Return the moves
    return moves

def f3(bottles, T):
    # Initialize variables
    current_bottle = 1
    total_liters = 0
    moves = []

    # Loop through the bottles
    while total_liters < T:
        # Check if the current bottle is full
        if bottles[current_bottle - 1] == 0:
            # If it is full, move to the next bottle
            current_bottle += 1
        else:
            # If it is not full, transfer dry ice from it into the target bottle
            moves.append(f"transfer {current_bottle} 0")
            total_liters += bottles[current_bottle - 1]

        # Check if the current bottle is the target bottle
        if current_bottle == 0:
            # If it is the target bottle, break the loop
            break

    # Return the moves
    return moves

def main():
    # Read the input
    N, T = map(int, input().split())
    bottles = list(map(int, input().split()))

    # Call the functions
    moves1 = f1(bottles, T)
    moves2 = f2(bottles, T)
    moves3 = f3(bottles, T)

    # Check if any of the moves are possible
    if len(moves1) == 0 and len(moves2) == 0 and len(moves3) == 0:
        print("impossible")
    else:
        # Print the moves
        print("\n".join(moves1 + moves2 + moves3))

if __name__ == '__main__':
    main()

