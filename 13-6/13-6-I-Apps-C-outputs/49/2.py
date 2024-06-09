
def solve(N, V, supervisors):
    # Initialize a set to store the types of jokes told by the invitees
    jokes = set()
    # Iterate over the direct supervisors
    for supervisor, employee in supervisors:
        # If the direct supervisor is not invited, do not include the employee in the party
        if supervisor not in V:
            continue
        # If the set of jokes told by the direct supervisor and the employee don't form a set of consecutive numbers, do not include the employee in the party
        if not is_consecutive(V[supervisor], V[employee]):
            continue
        # Add the type of joke told by the employee to the set
        jokes.add(V[employee])
    # Return the number of different sets of jokes
    return len(jokes)

def is_consecutive(a, b):
    # Sort the two numbers in ascending order
    a, b = sorted([a, b])
    # Return True if the difference between the two numbers is exactly 1
    return b == a + 1

