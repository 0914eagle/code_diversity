
def get_badge_numbers(N, L, B, S, D, locks):
    # Initialize a set to store the badge numbers that can pass from S to D
    badge_numbers = set()

    # Iterate through each lock
    for lock in locks:
        # Extract the information from the lock
        a, b, x, y = lock

        # Check if the lock is between S and D
        if a == S and b == D:
            # Add the badge numbers to the set
            badge_numbers |= set(range(x, y + 1))

    # Return the number of badge numbers in the set
    return len(badge_numbers)

if __name__ == "__main__":
    # Read the input
    N, L, B, S, D = map(int, input().split())
    locks = []
    for _ in range(L):
        locks.append(list(map(int, input().split())))

    # Call the function to get the number of badge numbers that can pass from S to D
    result = get_badge_numbers(N, L, B, S, D, locks)

    # Print the result
    print(result)

