
def get_number_of_different_sets_of_jokes(N, V, supervisors):
    # Initialize a set to store the types of jokes told by the invitees
    jokes = set()
    
    # Add the types of jokes told by Petar, which is the CEO and has the label 1
    jokes.add(V[0])
    
    # Iterate through the list of supervisors
    for supervisor, subordinate in supervisors:
        # If the subordinate is not invited, skip this iteration
        if subordinate not in jokes:
            continue
        
        # Add the type of joke told by the subordinate to the set of jokes
        jokes.add(V[subordinate])
    
    # Return the number of different sets of jokes
    return len(jokes)

def main():
    N = int(input())
    V = list(map(int, input().split()))
    supervisors = []
    for _ in range(N-1):
        supervisor, subordinate = map(int, input().split())
        supervisors.append((supervisor, subordinate))
    print(get_number_of_different_sets_of_jokes(N, V, supervisors))

if __name__ == '__main__':
    main()

