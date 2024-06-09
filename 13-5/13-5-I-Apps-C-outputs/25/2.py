
def solve(N, numbers):
    # Initialize a set to store the numbers that Ivana can take
    ivana_moves = set()

    # Iterate through the numbers and find the ones that are adjacent to each other
    for i in range(N):
        if i + 1 < N and numbers[i] + 1 == numbers[i + 1]:
            ivana_moves.add(numbers[i])
        if i - 1 >= 0 and numbers[i] - 1 == numbers[i - 1]:
            ivana_moves.add(numbers[i])

    # Return the number of unique moves that Ivana can make
    return len(ivana_moves)

