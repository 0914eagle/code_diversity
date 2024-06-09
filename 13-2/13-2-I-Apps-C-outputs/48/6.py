
def solve(N, V, A, B):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the employees who are not invited
    not_invited_jokes = set()
    # Iterate over the direct supervisors and their employees
    for supervisor, employee in zip(A, B):
        # If the employee is not invited, add their type of joke to the set of not invited jokes
        if employee not in invited_jokes:
            not_invited_jokes.add(V[employee - 1])
        # If the supervisor is not invited, add their type of joke to the set of not invited jokes
        if supervisor not in invited_jokes:
            not_invited_jokes.add(V[supervisor - 1])
    # Iterate over the employees and their supervisors
    for employee, supervisor in zip(A, B):
        # If the employee is invited, add their type of joke to the set of invited jokes
        if employee in invited_jokes:
            invited_jokes.add(V[employee - 1])
        # If the supervisor is invited, add their type of joke to the set of invited jokes
        if supervisor in invited_jokes:
            invited_jokes.add(V[supervisor - 1])
    # Return the number of different sets of jokes that comply to the constraints
    return len(invited_jokes)

