
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()

    # Iterate through the list of employees and their supervisors
    for i in range(N):
        # If the employee is not Petar, check if their supervisor is invited
        if i != 1 and A[i] not in invited_jokes:
            continue
        # If the employee is not Petar, check if the set of jokes told by their supervisor and their direct supervisor form a set of consecutive numbers
        if i != 1 and not is_consecutive(invited_jokes, V[A[i]]):
            continue
        # If the employee is not Petar, check if the set of jokes told by their supervisor and their direct supervisor form a set of consecutive numbers
        if i != 1 and not is_consecutive(invited_jokes, V[B[i]]):
            continue
        # If the employee is Petar, or if their supervisor and direct supervisor form a set of consecutive numbers, add the employee to the set of invited employees
        invited_jokes.add(V[i])

    # Return the number of different sets of jokes told by the invited employees
    return len(invited_jokes)

# Check if the set of jokes forms a set of consecutive numbers
def is_consecutive(jokes, joke):
    # If the set of jokes is empty, return True
    if not jokes:
        return True
    # Get the minimum and maximum values in the set of jokes
    min_joke = min(jokes)
    max_joke = max(jokes)
    # If the joke is within the range of the minimum and maximum values in the set of jokes, return True
    if min_joke <= joke <= max_joke:
        return True
    # If the joke is not within the range of the minimum and maximum values in the set of jokes, return False
    return False

# Test the solve function with the sample input
N = 4
V = [2, 1, 3, 4]
A = [1, 2, 1, 3]
B = [1, 3, 2, 4]
print(solve(N, V, A, B))

