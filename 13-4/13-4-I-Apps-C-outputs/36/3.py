
def read_input():
    N = int(input())
    V = list(map(int, input().split()))
    supervisors = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        supervisors.append((a, b))
    return N, V, supervisors

def f1(N, V, supervisors):
    # find all the direct supervisors for each employee
    direct_supervisors = {}
    for a, b in supervisors:
        if a not in direct_supervisors:
            direct_supervisors[a] = []
        direct_supervisors[a].append(b)
    
    # find all the indirect supervisors for each employee
    indirect_supervisors = {}
    for a, b in supervisors:
        if b not in indirect_supervisors:
            indirect_supervisors[b] = []
        indirect_supervisors[b].append(a)
    
    # find all the sets of jokes that comply to the constraints
    sets = []
    for i in range(1, N+1):
        # check if the person i is directly or indirectly supervised by the CEO
        if i in direct_supervisors[1] or i in indirect_supervisors[1]:
            # check if the person i tells a new type of joke
            if V[i-1] not in sets:
                sets.append(V[i-1])
    
    return len(sets)

def f2(N, V, supervisors):
    # find all the direct supervisors for each employee
    direct_supervisors = {}
    for a, b in supervisors:
        if a not in direct_supervisors:
            direct_supervisors[a] = []
        direct_supervisors[a].append(b)
    
    # find all the indirect supervisors for each employee
    indirect_supervisors = {}
    for a, b in supervisors:
        if b not in indirect_supervisors:
            indirect_supervisors[b] = []
        indirect_supervisors[b].append(a)
    
    # find all the sets of jokes that comply to the constraints
    sets = []
    for i in range(1, N+1):
        # check if the person i is directly or indirectly supervised by the CEO
        if i in direct_supervisors[1] or i in indirect_supervisors[1]:
            # check if the person i tells a new type of joke
            if V[i-1] not in sets:
                sets.append(V[i-1])
    
    # find all the sets of consecutive numbers
    consecutive_sets = []
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            if sets[j] - sets[i] == j - i:
                consecutive_sets.append(sets[i:j+1])
    
    return len(consecutive_sets)

if __name__ == '__main__':
    N, V, supervisors = read_input()
    print(f1(N, V, supervisors))
    print(f2(N, V, supervisors))

