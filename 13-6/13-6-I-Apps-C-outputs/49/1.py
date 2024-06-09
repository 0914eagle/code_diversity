
def solve(N, V, direct_supervisors):
    # Initialize a set to store the types of jokes told by the invited guests
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the uninvited guests
    uninvited_jokes = set()
    # Iterate over the direct supervisors
    for supervisor, employee in direct_supervisors:
        # If the supervisor is not invited, add the type of joke told by the employee to the uninvited jokes set
        if supervisor not in invited_jokes:
            uninvited_jokes.add(V[employee - 1])
        # If the employee is not invited, add the type of joke told by the employee to the uninvited jokes set
        if employee not in invited_jokes:
            uninvited_jokes.add(V[supervisor - 1])
    
    # Initialize a set to store the consecutive sets of jokes
    consecutive_sets = set()
    # Iterate over the uninvited jokes
    for joke in uninvited_jokes:
        # If the joke is not already in the invited jokes set, add it to the invited jokes set
        if joke not in invited_jokes:
            invited_jokes.add(joke)
            # Check if the set of jokes is consecutive
            if is_consecutive(invited_jokes):
                consecutive_sets.add(frozenset(invited_jokes))
            # If the set of jokes is not consecutive, remove the last joke added to the set
            else:
                invited_jokes.remove(joke)
    
    return len(consecutive_sets)

def is_consecutive(jokes):
    # Sort the jokes in ascending order
    sorted_jokes = sorted(jokes)
    # Iterate over the jokes
    for i in range(len(sorted_jokes) - 1):
        # If the difference between the current joke and the next joke is not 1, return False
        if sorted_jokes[i + 1] - sorted_jokes[i] != 1:
            return False
    return True

def main():
    N = int(input())
    V = list(map(int, input().split()))
    direct_supervisors = []
    for _ in range(N - 1):
        direct_supervisors.append(list(map(int, input().split())))
    print(solve(N, V, direct_supervisors))

if __name__ == "__main__":
    main()

