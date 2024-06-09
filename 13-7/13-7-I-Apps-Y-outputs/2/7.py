
def solve(n):
    # Initialize a set to store the numbers that can be obtained in 1 move
    one_moves = set()
    # Initialize a set to store the numbers that can be obtained in 2 moves
    two_moves = set()
    # Initialize a set to store the numbers that can be obtained in 3 moves
    three_moves = set()
    # Add 1 to the set of numbers that can be obtained in 1 move
    one_moves.add(1)
    # Iterate until the set of numbers that can be obtained in 1 move is empty
    while one_moves:
        # Initialize a set to store the numbers that can be obtained in the next move
        next_moves = set()
        # Iterate over the numbers that can be obtained in 1 move
        for num in one_moves:
            # If the number is divisible by 2, add the result of the division to the set of numbers that can be obtained in the next move
            if num % 2 == 0:
                next_moves.add(num // 2)
            # If the number is divisible by 3, add the result of the division to the set of numbers that can be obtained in the next move
            if num % 3 == 0:
                next_moves.add(num // 3)
            # If the number is divisible by 5, add the result of the division to the set of numbers that can be obtained in the next move
            if num % 5 == 0:
                next_moves.add(num // 5)
        # Add the numbers that can be obtained in the next move to the set of numbers that can be obtained in 2 moves
        two_moves.update(next_moves)
        # Empty the set of numbers that can be obtained in 1 move
        one_moves.clear()
        # Add the numbers that can be obtained in the next move to the set of numbers that can be obtained in 1 move
        one_moves.update(next_moves)
    # If the set of numbers that can be obtained in 2 moves is not empty, return the minimum number of moves required to obtain 1
    if two_moves:
        return 2
    # If the set of numbers that can be obtained in 3 moves is not empty, return the minimum number of moves required to obtain 1
    if three_moves:
        return 3
    # Otherwise, return -1
    return -1

