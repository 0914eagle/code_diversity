
def solve(N, V, direct_supervisors):
    # Initialize a set to store the types of jokes told by the invited guests
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the direct supervisors of the invited guests
    direct_supervisor_jokes = set()
    # Initialize a set to store the types of jokes told by the indirect supervisors of the invited guests
    indirect_supervisor_jokes = set()

    # Iterate through the direct supervisors and their respective supervisors
    for direct_supervisor, supervisor in direct_supervisors:
        # If the direct supervisor is not invited, continue to the next iteration
        if direct_supervisor not in invited_jokes:
            continue
        # If the direct supervisor's supervisor is not invited, continue to the next iteration
        if supervisor not in invited_jokes:
            continue
        # Add the type of joke told by the direct supervisor to the set of jokes told by their supervisor
        indirect_supervisor_jokes.add(V[supervisor - 1])

    # Iterate through the guests and check if they are invited
    for guest in range(1, N + 1):
        # If the guest is not invited, continue to the next iteration
        if guest not in invited_jokes:
            continue
        # If the guest's type of joke is not consecutive with the types of jokes told by their direct supervisors, continue to the next iteration
        if guest - 1 not in direct_supervisor_jokes and guest + 1 not in direct_supervisor_jokes:
            continue
        # If the guest's type of joke is not consecutive with the types of jokes told by their indirect supervisors, continue to the next iteration
        if guest - 1 not in indirect_supervisor_jokes and guest + 1 not in indirect_supervisor_jokes:
            continue
        # Add the type of joke told by the guest to the set of jokes seen at the party
        invited_jokes.add(V[guest - 1])

    # Return the number of different sets of jokes seen at the party
    return len(invited_jokes)

