
def solve(n, a):
    # Initialize the minimum number of seconds as 0
    seconds = 0

    # Initialize a set to store the positive chocolate pieces
    positive_pieces = set()

    # Iterate through the input array
    for i in range(n):
        # If the current piece is positive, add it to the set of positive pieces
        if a[i] > 0:
            positive_pieces.add(a[i])

    # If there is only one positive piece, return -1 because Alice won't be happy
    if len(positive_pieces) == 1:
        return -1

    # Iterate through the set of positive pieces
    for piece in positive_pieces:
        # Find the greatest common divisor of the current piece and all other positive pieces
        gcd = piece
        for other_piece in positive_pieces:
            gcd = math.gcd(gcd, other_piece)

        # If the GCD is 1, return -1 because Alice won't be happy
        if gcd == 1:
            return -1

        # Increment the minimum number of seconds by the number of seconds it would take to make the current piece divisible by the GCD
        seconds += piece // gcd

    # Return the minimum number of seconds
    return seconds

