
def solve(N, V, A, B):
    # Initialize a dictionary to store the jokes told by each person
    jokes = {i: set() for i in range(1, N+1)}
    # Add the jokes told by each person to the dictionary
    for i in range(N):
        jokes[i+1].add(V[i])

    # Initialize a set to store the jokes that can be told at the party
    possible_jokes = set()

    # Iterate through each person and their supervisor
    for i in range(1, N+1):
        # If the person is not Petar (i.e., has a label other than 1)
        if i != 1:
            # Get the jokes told by the person's supervisor
            supervisor_jokes = jokes[A[i-1]]
            # Get the jokes told by the person
            person_jokes = jokes[i]
            # Check if the jokes are consecutive
            if len(supervisor_jokes.union(person_jokes)) == len(set(range(min(supervisor_jokes), max(person_jokes)+1))):
                # If they are consecutive, add the jokes to the set of possible jokes
                possible_jokes = possible_jokes.union(person_jokes)

    # Return the number of different sets of jokes that can be told at the party
    return len(possible_jokes)

