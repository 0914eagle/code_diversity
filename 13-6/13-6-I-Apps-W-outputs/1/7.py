
def solve(n, x):
    # Initialize a list to store the moves
    moves = []
    # Set the starting position of Alice and Bob
    alice = 1
    bob = x
    # Loop until Alice and Bob are at the same position
    while alice != bob:
        # Bob moves first
        bob = moves.pop() if moves else 1
        # Alice moves
        alice = bob + 1 if alice % n != 0 else 1
        # Add Bob's move to the list
        moves.append(bob)
    # Return the total number of moves
    return len(moves) + 1

