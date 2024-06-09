
def solve(n):
    # Initialize a set to store the numbers that can be obtained in 1 move
    one_moves = set([1])
    # Initialize a set to store the numbers that can be obtained in 2 moves
    two_moves = set([2, 3, 5])
    # Initialize a set to store the numbers that can be obtained in 3 moves
    three_moves = set([4, 6, 10])
    # Initialize a set to store the numbers that can be obtained in 4 moves
    four_moves = set([8, 9, 12, 15])
    # Initialize a set to store the numbers that can be obtained in 5 moves
    five_moves = set([16, 18, 20, 24, 27])
    # Initialize a set to store the numbers that can be obtained in 6 moves
    six_moves = set([32, 36, 40, 48, 54, 60])
    # Initialize a set to store the numbers that can be obtained in 7 moves
    seven_moves = set([64, 72, 80, 96, 108, 120, 144])

    # Loop until the number is 1
    while n != 1:
        # If the number is already in the one_moves set, return the number of moves
        if n in one_moves:
            return len(one_moves)
        # If the number is already in the two_moves set, return the number of moves
        if n in two_moves:
            return len(two_moves)
        # If the number is already in the three_moves set, return the number of moves
        if n in three_moves:
            return len(three_moves)
        # If the number is already in the four_moves set, return the number of moves
        if n in four_moves:
            return len(four_moves)
        # If the number is already in the five_moves set, return the number of moves
        if n in five_moves:
            return len(five_moves)
        # If the number is already in the six_moves set, return the number of moves
        if n in six_moves:
            return len(six_moves)
        # If the number is already in the seven_moves set, return the number of moves
        if n in seven_moves:
            return len(seven_moves)

        # If the number is divisible by 2, divide it by 2 and add it to the two_moves set
        if n % 2 == 0:
            n //= 2
            two_moves.add(n)
        # If the number is divisible by 3, divide it by 3 and add it to the three_moves set
        elif n % 3 == 0:
            n //= 3
            three_moves.add(n)
        # If the number is divisible by 5, divide it by 5 and add it to the five_moves set
        elif n % 5 == 0:
            n //= 5
            five_moves.add(n)
        # If the number is not divisible by 2, 3, or 5, it is not possible to obtain 1
        else:
            return -1

    # If the number is 1, return the number of moves
    return len(one_moves)

