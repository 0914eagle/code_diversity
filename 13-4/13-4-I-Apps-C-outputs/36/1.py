
def read_input():
    N = int(input())
    V = list(map(int, input().split()))
    direct_supervisors = []
    for _ in range(N-1):
        direct_supervisors.append(list(map(int, input().split())))
    return N, V, direct_supervisors

def f1(N, V, direct_supervisors):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the employees who are not invited
    not_invited_jokes = set(V[1:])
    # Initialize a set to store the types of jokes told by the employees who are directly or indirectly supervised by the CEO
    ceo_jokes = set()
    
    # Iterate through the direct supervisors and add the types of jokes told by the employees who are directly supervised by the CEO
    for direct_supervisor in direct_supervisors:
        ceo_jokes.add(V[direct_supervisor[0]-1])
    
    # Iterate through the employees and add the types of jokes told by the invited employees to the invited_jokes set
    for i in range(1, N):
        if V[i] in ceo_jokes:
            invited_jokes.add(V[i])
    
    # Return the number of different sets of jokes that comply to the constraints
    return len(invited_jokes)

def f2(N, V, direct_supervisors):
    # Initialize a set to store the types of jokes told by the invited employees
    invited_jokes = set()
    # Initialize a set to store the types of jokes told by the employees who are not invited
    not_invited_jokes = set(V[1:])
    # Initialize a set to store the types of jokes told by the employees who are directly or indirectly supervised by the CEO
    ceo_jokes = set()
    
    # Iterate through the direct supervisors and add the types of jokes told by the employees who are directly supervised by the CEO
    for direct_supervisor in direct_supervisors:
        ceo_jokes.add(V[direct_supervisor[0]-1])
    
    # Iterate through the employees and add the types of jokes told by the invited employees to the invited_jokes set
    for i in range(1, N):
        if V[i] in ceo_jokes:
            invited_jokes.add(V[i])
    
    # Return the number of different sets of jokes that comply to the constraints
    return len(invited_jokes)

if __name__ == '__main__':
    N, V, direct_supervisors = read_input()
    print(f1(N, V, direct_supervisors))
    print(f2(N, V, direct_supervisors))

