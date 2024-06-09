
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
        # If the employee is a direct supervisor, add their joke to the set of direct supervisor jokes
        if i in B:
            direct_supervisor_jokes.add(V[i])
        # If the employee is an indirect supervisor, add their joke to the set of indirect supervisor jokes
        for j in range(N):
            if B[j] == i:
                indirect_supervisor_jokes.add(V[j])

    # Initialize a set to store the consecutive sets of jokes
    consecutive_jokes = set()

    # Iterate through the set of invited jokes
    for i in invited_jokes:
        # If the invited joke is not in the set of direct supervisor jokes, add it to the set of consecutive jokes
        if i not in direct_supervisor_jokes:
            consecutive_jokes.add(i)
        # If the invited joke is in the set of direct supervisor jokes, check if it is in the set of indirect supervisor jokes
        elif i in direct_supervisor_jokes and i in indirect_supervisor_jokes:
            # If the invited joke is in the set of indirect supervisor jokes, add it to the set of consecutive jokes
            consecutive_jokes.add(i)

    # Return the number of consecutive sets of jokes
    return len(consecutive_jokes)

