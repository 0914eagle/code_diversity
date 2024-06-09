
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by the employees
    jokes = set()

    # Add the types of jokes told by the employees to the set
    for i in range(N):
        jokes.add(V[i])

    # Initialize a dictionary to store the direct supervisors of each employee
    supervisors = {}

    # Add the direct supervisors of each employee to the dictionary
    for i in range(N-1):
        supervisors[A[i]] = B[i]

    # Initialize a set to store the types of jokes that can be told at the party
    party_jokes = set()

    # Add the types of jokes told by the employees to the set
    for i in range(N):
        party_jokes.add(V[i])

    # Initialize a variable to store the number of different sets of jokes that can be told at the party
    num_party_jokes = 0

    # Iterate over the types of jokes told by the employees
    for i in range(N):
        # If the type of joke is not already in the set of jokes that can be told at the party
        if V[i] not in party_jokes:
            # Add the type of joke to the set of jokes that can be told at the party
            party_jokes.add(V[i])
            num_party_jokes += 1

    # Return the number of different sets of jokes that can be told at the party
    return num_party_jokes

