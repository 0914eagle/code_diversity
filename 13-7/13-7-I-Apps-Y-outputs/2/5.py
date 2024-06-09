
def solve(n):
    # Initialize a set to store the numbers that can be obtained in one move
    one_moves = set([1])
    # Initialize a set to store the numbers that can be obtained in two moves
    two_moves = set([1])
    # Initialize a set to store the numbers that can be obtained in three moves
    three_moves = set([1])
    # Initialize a set to store the numbers that can be obtained in four moves
    four_moves = set([1])
    # Initialize a set to store the numbers that can be obtained in five moves
    five_moves = set([1])

    # Loop until the number is 1 or cannot be obtained in five moves
    while n != 1 and n not in five_moves:
        # If the number is divisible by 2, add it to the one_moves set
        if n % 2 == 0:
            one_moves.add(n // 2)
        # If the number is divisible by 3, add it to the two_moves set
        if n % 3 == 0:
            two_moves.add(n // 3)
        # If the number is divisible by 5, add it to the three_moves set
        if n % 5 == 0:
            three_moves.add(n // 5)
        # If the number is divisible by 2 and 3, add it to the four_moves set
        if n % 6 == 0:
            four_moves.add(n // 6)
        # If the number is divisible by 2, 3, and 5, add it to the five_moves set
        if n % 30 == 0:
            five_moves.add(n // 30)

        # Add the current number to the one_moves set
        one_moves.add(n)

        # Check if the number can be obtained in one move
        if n in one_moves:
            return 1
        # Check if the number can be obtained in two moves
        elif n in two_moves:
            return 2
        # Check if the number can be obtained in three moves
        elif n in three_moves:
            return 3
        # Check if the number can be obtained in four moves
        elif n in four_moves:
            return 4
        # Check if the number can be obtained in five moves
        elif n in five_moves:
            return 5
        # If the number cannot be obtained in five moves, return -1
        else:
            return -1

    # If the number is 1, return 0
    if n == 1:
        return 0

    # If the number cannot be obtained in five moves, return -1
    return -1

