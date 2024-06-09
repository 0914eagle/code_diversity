
def solve(N, numbers):
    # Initialize a set to store the numbers that Ivana can take
    ivana_moves = set()

    # Iterate through the numbers and find the ones that are adjacent to the first number
    for i in range(N):
        if i != 0 and numbers[i] - numbers[i-1] == 1:
            ivana_moves.add(numbers[i])

    # Return the length of the set
    return len(ivana_moves)

