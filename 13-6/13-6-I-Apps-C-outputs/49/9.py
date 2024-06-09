
def solve(N, V, edges):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the employees directly or indirectly supervised by the CEO
    ceo_jokes = set()
    # Initialize a dictionary to map each employee to their supervisor
    supervisors = {}

    # Populate the dictionary with the given data
    for i in range(1, N+1):
        supervisors[i] = i
    for edge in edges:
        supervisors[edge[1]] = edge[0]

    # Iterate through the employees and check if they are eligible to be invited
    for i in range(1, N+1):
        # If the employee is not the CEO, check if their supervisor is invited
        if i != 1 and supervisors[i] not in invited_jokes:
            continue
        # If the employee is eligible, add their type of joke to the set of invited jokes
        invited_jokes.add(V[i-1])
        # If the employee is the CEO, add their type of joke to the set of jokes told by the CEO and their direct or indirect supervisors
        if i == 1:
            ceo_jokes.add(V[i-1])

    # Count the number of different sets of jokes that comply to the constraints
    count = 0
    for i in range(1, N+1):
        # If the employee is not invited, skip them
        if i not in invited_jokes:
            continue
        # If the employee is invited, check if the set of jokes told by their direct or indirect supervisors forms a consecutive sequence
        consecutive = True
        for j in range(1, N+1):
            if j in invited_jokes and (V[j-1] - V[i-1] != 1):
                consecutive = False
                break
        # If the set of jokes forms a consecutive sequence, increment the count
        if consecutive:
            count += 1

    return count

