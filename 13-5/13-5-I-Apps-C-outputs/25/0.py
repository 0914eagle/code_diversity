
def solve(n, numbers):
    # Initialize a set to store the numbers that Ivana can take as her first move
    ivana_moves = set()

    # Iterate through the numbers and check if they are odd
    for i in range(n):
        if numbers[i] % 2 == 1:
            ivana_moves.add(i)

    # Return the length of the set, which is the number of different first moves Ivana can make
    return len(ivana_moves)

