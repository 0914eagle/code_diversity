
def solve(n, jokes, supervisors):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the direct supervisors of the invited employees
    direct_supervisor_jokes = set()
    # Initialize a set to store the types of jokes told by the indirect supervisors of the invited employees
    indirect_supervisor_jokes = set()

    # Iterate through the list of jokes told by each employee
    for i in range(n):
        # If the employee is invited, add their joke to the set of invited jokes
        if i in supervisors[0]:
            invited_jokes.add(jokes[i])
        # If the employee is a direct supervisor, add their joke to the set of direct supervisor jokes
        for supervisor in supervisors:
            if i == supervisor[0]:
                direct_supervisor_jokes.add(jokes[i])
        # If the employee is an indirect supervisor, add their joke to the set of indirect supervisor jokes
        for supervisor in supervisors:
            if i in supervisor[1:]:
                indirect_supervisor_jokes.add(jokes[i])

    # Initialize a set to store the consecutive sets of jokes
    consecutive_jokes = set()

    # Iterate through the set of invited jokes
    for joke in invited_jokes:
        # If the joke is not already in the set of consecutive jokes, add it to the set
        if joke not in consecutive_jokes:
            consecutive_jokes.add(joke)
        # If the joke is already in the set of consecutive jokes, find the largest consecutive set of jokes that includes the current joke
        else:
            largest_consecutive_set = find_largest_consecutive_set(consecutive_jokes, joke)
            # If the largest consecutive set of jokes includes the direct supervisor jokes, add the direct supervisor jokes to the set of consecutive jokes
            if direct_supervisor_jokes.issubset(largest_consecutive_set):
                consecutive_jokes.update(direct_supervisor_jokes)
            # If the largest consecutive set of jokes includes the indirect supervisor jokes, add the indirect supervisor jokes to the set of consecutive jokes
            if indirect_supervisor_jokes.issubset(largest_consecutive_set):
                consecutive_jokes.update(indirect_supervisor_jokes)

    return len(consecutive_jokes)

def find_largest_consecutive_set(consecutive_jokes, joke):
    # Initialize a set to store the consecutive set of jokes that includes the current joke
    current_consecutive_set = set()
    # Iterate through the set of consecutive jokes
    for consecutive_joke in consecutive_jokes:
        # If the current joke is adjacent to the current consecutive set of jokes, add it to the set
        if consecutive_joke - 1 == joke or consecutive_joke + 1 == joke:
            current_consecutive_set.add(consecutive_joke)
    return current_consecutive_set

