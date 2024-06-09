
def solve(n, numbers):
    # Initialize a set to store the numbers that Ivana can take as her first move
    ivana_moves = set()

    # Iterate through the numbers and find the ones that are adjacent to the first number
    for i in range(1, n):
        if numbers[i] - numbers[0] in numbers:
            ivana_moves.add(numbers[i] - numbers[0])

    # Return the length of the set, which is the number of different first moves Ivana can make
    return len(ivana_moves)

