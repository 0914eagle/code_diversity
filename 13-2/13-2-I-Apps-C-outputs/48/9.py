
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the direct supervisors of the invited employees
    direct_supervisor_jokes = set()
    # Initialize a set to store the types of jokes told by the indirect supervisors of the invited employees
    indirect_supervisor_jokes = set()

    # Iterate through the list of employees and their jokes
    for i in range(N):
        # If the employee is invited, add their joke to the set of invited jokes
        if i in A:
            invited_jokes.add(V[i])
        # If the employee is not invited, add their joke to the set of direct supervisor jokes
        else:
            direct_supervisor_jokes.add(V[i])

    # Iterate through the list of direct supervisors and their jokes
    for i in range(N):
        # If the direct supervisor is invited, add their joke to the set of indirect supervisor jokes
        if i in A:
            indirect_supervisor_jokes.add(V[i])

    # Initialize a set to store the consecutive sets of jokes
    consecutive_sets = set()

    # Iterate through the list of invited jokes
    for i in invited_jokes:
        # If the invited joke is not in the set of direct supervisor jokes, add it to the set of consecutive sets
        if i not in direct_supervisor_jokes:
            consecutive_sets.add(i)
        # If the invited joke is in the set of direct supervisor jokes, add it to the set of consecutive sets if it is consecutive with the previous joke
        else:
            previous_joke = max(consecutive_sets)
            if i == previous_joke + 1:
                consecutive_sets.add(i)

    # Return the number of consecutive sets of jokes
    return len(consecutive_sets)

