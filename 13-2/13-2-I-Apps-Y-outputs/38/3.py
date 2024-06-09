
def solve(N, M):
    # Initialize a set to store the even numbers
    even_numbers = set()

    # Add all even numbers from 2 to 2N to the set
    for i in range(2, 2 * N + 1, 2):
        even_numbers.add(i)

    # Add all odd numbers from 1 to 2M to the set
    for i in range(1, 2 * M + 1, 2):
        even_numbers.add(i)

    # Return the number of pairs of numbers that have a sum that is even
    return len(even_numbers)

