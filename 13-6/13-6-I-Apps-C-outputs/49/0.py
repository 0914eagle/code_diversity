
def solve(N, V, supervisors):
    # Initialize a set to store the types of jokes seen
    jokes_seen = set()
    # Initialize a set to store the types of jokes told by the CEO
    ceo_jokes = set(V[0])
    # Initialize a dictionary to store the direct supervisors of each employee
    direct_supervisors = {i: supervisors[i-1] for i in range(1, N+1)}
    # Initialize a dictionary to store the types of jokes told by each employee
    employee_jokes = {i: set(V[i-1]) for i in range(1, N+1)}

    # Iterate through the employees in the company
    for employee in range(1, N+1):
        # If the employee is not the CEO, check if their direct supervisor is invited
        if employee != 1 and direct_supervisors[employee] not in jokes_seen:
            continue
        # If the employee is the CEO or their direct supervisor is invited, add their jokes to the set of jokes seen
        jokes_seen.update(employee_jokes[employee])

    # Return the number of different sets of jokes seen
    return len(jokes_seen)

