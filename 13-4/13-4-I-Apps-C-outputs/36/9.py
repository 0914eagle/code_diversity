
def f1(N, V, A, B):
    # f1(N, V, A, B) takes in N, the number of employees, V, the types of jokes each employee tells, A, the direct supervisors of each employee, and B, the inverse of A
    # f1 returns the number of different sets of jokes that comply to the constraints
    
    # initialize variables
    num_jokes = len(set(V))
    jokes = set(V)
    supervisors = set(A)
    subordinates = set(B)
    valid_jokes = set()
    
    # add jokes told by supervisors
    for supervisor in supervisors:
        valid_jokes.add(V[supervisor-1])
    
    # add jokes told by subordinates
    for subordinate in subordinates:
        valid_jokes.add(V[subordinate-1])
    
    # add jokes that are consecutive
    for i in range(num_jokes):
        for j in range(i+1, num_jokes):
            if V[i] + 1 == V[j]:
                valid_jokes.add(V[i])
                valid_jokes.add(V[j])
    
    return len(valid_jokes)

def f2(N, V, A, B):
    # f2(N, V, A, B) takes in N, the number of employees, V, the types of jokes each employee tells, A, the direct supervisors of each employee, and B, the inverse of A
    # f2 returns the number of different sets of jokes that comply to the constraints
    
    # initialize variables
    num_jokes = len(set(V))
    jokes = set(V)
    supervisors = set(A)
    subordinates = set(B)
    valid_jokes = set()
    
    # add jokes told by supervisors
    for supervisor in supervisors:
        valid_jokes.add(V[supervisor-1])
    
    # add jokes told by subordinates
    for subordinate in subordinates:
        valid_jokes.add(V[subordinate-1])
    
    # add jokes that are consecutive
    for i in range(num_jokes):
        for j in range(i+1, num_jokes):
            if V[i] + 1 == V[j]:
                valid_jokes.add(V[i])
                valid_jokes.add(V[j])
    
    return len(valid_jokes)

if __name__ == '__main__':
    N = int(input())
    V = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f1(N, V, A, B))
    print(f2(N, V, A, B))

