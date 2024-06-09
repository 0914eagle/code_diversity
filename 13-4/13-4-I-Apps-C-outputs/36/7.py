
def get_jokes_sets(jokes, supervisors):
    # Initialize a set to store the jokes told by the invited employees
    invited_jokes = set()
    
    # Initialize a set to store the jokes told by the direct supervisors of the invited employees
    direct_supervisor_jokes = set()
    
    # Iterate through the employees and their jokes
    for employee, joke in enumerate(jokes, start=1):
        # If the employee is not the CEO (i.e., not the first employee), check if their direct supervisor is invited
        if employee != 1 and supervisors[employee-1] not in invited_jokes:
            # If the direct supervisor is not invited, do not include the employee in the party
            continue
        
        # If the employee is invited, add their joke to the set of invited jokes
        invited_jokes.add(joke)
        
        # If the employee is not the CEO, add their direct supervisor's joke to the set of direct supervisor jokes
        if employee != 1:
            direct_supervisor_jokes.add(jokes[supervisors[employee-1]-1])
    
    # Initialize a set to store the consecutive sets of jokes
    consecutive_sets = set()
    
    # Iterate through the invited jokes and check if they form a consecutive set
    for i in range(len(invited_jokes)):
        # If the current joke is not the first joke in the set, check if the difference between the current joke and the previous joke is 1
        if i != 0 and invited_jokes[i] - invited_jokes[i-1] != 1:
            # If the difference is not 1, start a new set
            consecutive_sets.add(frozenset(invited_jokes[i-1:i+1]))
        # If the current joke is the first joke in the set, start a new set
        else:
            consecutive_sets.add(frozenset(invited_jokes[i:i+1]))
    
    # Return the number of consecutive sets
    return len(consecutive_sets)

def main():
    # Read the number of employees and their jokes from stdin
    n = int(input())
    jokes = list(map(int, input().split()))
    
    # Read the direct supervisors of the employees from stdin
    supervisors = [int(input()) for _ in range(n-1)]
    
    # Call the get_jokes_sets function to get the number of consecutive sets of jokes
    result = get_jokes_sets(jokes, supervisors)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

