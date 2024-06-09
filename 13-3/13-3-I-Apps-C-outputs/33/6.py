
def f1(N, volumes, T):
    # Initialize the variables
    bottles = [0] * N
    current_bottle = 0
    total_volume = 0
    moves = []

    # Fill the first bottle with dry ice
    moves.append(f"fill {current_bottle + 1}")
    bottles[current_bottle] = volumes[current_bottle]
    total_volume += volumes[current_bottle]

    # Loop until the target volume is reached
    while total_volume < T:
        # If the current bottle is full, discard it and move to the next one
        if bottles[current_bottle] == volumes[current_bottle]:
            moves.append(f"discard {current_bottle + 1}")
            current_bottle = (current_bottle + 1) % N

        # Fill the current bottle with dry ice
        moves.append(f"fill {current_bottle + 1}")
        bottles[current_bottle] = volumes[current_bottle]
        total_volume += volumes[current_bottle]

        # Transfer dry ice from the current bottle to the next one
        moves.append(f"transfer {current_bottle + 1} {current_bottle + 2}")
        bottles[current_bottle + 1] += bottles[current_bottle]
        bottles[current_bottle] = 0

    # Return the moves
    return moves

def f2(N, volumes, T):
    # Initialize the variables
    bottles = [0] * N
    current_bottle = 0
    total_volume = 0
    moves = []

    # Fill the first bottle with dry ice
    moves.append(f"fill {current_bottle + 1}")
    bottles[current_bottle] = volumes[current_bottle]
    total_volume += volumes[current_bottle]

    # Loop until the target volume is reached
    while total_volume < T:
        # If the current bottle is full, discard it and move to the next one
        if bottles[current_bottle] == volumes[current_bottle]:
            moves.append(f"discard {current_bottle + 1}")
            current_bottle = (current_bottle + 1) % N

        # Fill the current bottle with dry ice
        moves.append(f"fill {current_bottle + 1}")
        bottles[current_bottle] = volumes[current_bottle]
        total_volume += volumes[current_bottle]

        # Transfer dry ice from the current bottle to the next one
        moves.append(f"transfer {current_bottle + 1} {current_bottle + 2}")
        bottles[current_bottle + 1] += bottles[current_bottle]
        bottles[current_bottle] = 0

    # Return the moves
    return moves

if __name__ == '__main__':
    N, volumes, T = map(int, input().split())
    volumes = list(map(int, input().split()))
    moves = f1(N, volumes, T)
    print(*moves, sep='\n')

