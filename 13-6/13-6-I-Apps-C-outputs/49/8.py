
def solve(N, V, A, B):
    # Initialize a dictionary to store the jokes told by each person
    jokes = {i: set() for i in range(1, N+1)}
    # Add the jokes told by each person to the dictionary
    for i in range(1, N+1):
        jokes[i].add(V[i-1])

    # Initialize a set to store the jokes that have been seen
    seen_jokes = set()

    # Iterate through each person and their supervisor
    for i in range(1, N+1):
        # If the person's supervisor is not invited, they cannot be invited
        if A[i-1] not in jokes:
            continue
        # If the set of jokes told by the person's supervisor and the person's jokes do not form a set of consecutive numbers, they cannot be invited
        if not is_consecutive(jokes[A[i-1]] | {V[i-1]}):
            continue
        # Add the person's jokes to the set of seen jokes
        seen_jokes |= jokes[i]

    # Return the number of different sets of jokes that have been seen
    return len(seen_jokes)

# Check if a set of numbers is consecutive
def is_consecutive(nums):
    return all(nums[i+1] == nums[i] + 1 for i in range(len(nums)-1))

