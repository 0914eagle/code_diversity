
def solve(N, M):
    # Initialize a set to store the even numbers
    even_numbers = set()

    # Add all even numbers from 2 to 2N to the set
    for i in range(2, 2*N+1, 2):
        even_numbers.add(i)

    # Add all odd numbers from 1 to M to the set
    for i in range(1, M+1, 2):
        even_numbers.add(i)

    # Return the length of the set, which is the number of ways to choose two balls with an even sum
    return len(even_numbers)

