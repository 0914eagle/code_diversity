
def solve(n, numbers):
    # Initialize a set to store the possible first moves
    first_moves = set()

    # Iterate through the numbers and find the adjacent numbers
    for i in range(n):
        # Find the adjacent numbers
        left = (i - 1) % n
        right = (i + 1) % n

        # Add the adjacent numbers to the set
        first_moves.add(numbers[left])
        first_moves.add(numbers[right])

    # Return the length of the set
    return len(first_moves)

