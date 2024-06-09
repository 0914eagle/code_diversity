
def solve(N, V, A, B):
    # Initialize a dictionary to store the jokes told by each person
    jokes = {i: set() for i in range(1, N+1)}

    # Add the jokes told by each person to the dictionary
    for i in range(N):
        jokes[i+1].add(V[i])

    # Initialize a set to store the jokes that have been seen
    seen = set()

    # Iterate through each person and their supervisor
    for i in range(N-1):
        # If the supervisor has not been invited, skip this person
        if A[i] not in jokes:
            continue

        # If the set of jokes told by the supervisor and the current person do not form a set of consecutive numbers, skip this person
        if not is_consecutive(jokes[A[i]] | jokes[i+1]):
            continue

        # Add the jokes told by the current person to the set of seen jokes
        seen |= jokes[i+1]

    # Return the number of different sets of jokes that have been seen
    return len(seen)

# Check if a set of numbers is consecutive
def is_consecutive(nums):
    return all(nums[i+1] - nums[i] == 1 for i in range(len(nums)-1))

