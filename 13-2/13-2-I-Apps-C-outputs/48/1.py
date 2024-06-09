
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
        # If the employee is not Petar, check if the set of jokes told by their direct supervisor and their jokes form a set of consecutive numbers
        if i != 1 and not is_consecutive(invited_jokes, V[i]):
            continue
        # If all conditions are met, add the employee's jokes to the set of invited jokes
        invited_jokes.add(V[i])

    # Return the number of different sets of jokes
    return len(invited_jokes)

# Check if the set of jokes forms a set of consecutive numbers
def is_consecutive(jokes, joke):
    # If the set of jokes is empty, return True
    if not jokes:
        return True
    # Get the minimum and maximum jokes in the set
    min_joke = min(jokes)
    max_joke = max(jokes)
    # Check if the joke is between the minimum and maximum jokes in the set
    return min_joke < joke < max_joke + 1

# Test the solve function with the sample input
N = 4
V = [2, 1, 3, 4]
A = [1, 2, 1, 3]
B = [2, 1, 3, 4]
print(solve(N, V, A, B))

