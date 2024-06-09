
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by each person
    jokes = set()
    # Add the jokes told by Petar (the CEO)
    jokes.add(V[0])
    # Iterate over the direct supervisors of each person
    for i in range(1, N):
        # If the direct supervisor of person i is also invited, add their joke to the set
        if V[i] in jokes:
            jokes.add(V[i])
    # Return the number of different sets of jokes
    return len(jokes)

