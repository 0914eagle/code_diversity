
def read_input():
    N = int(input())
    V = list(map(int, input().split()))
    supervisors = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        supervisors.append((a, b))
    return N, V, supervisors

def f1(N, V, supervisors):
    # find all the direct and indirect supervisors of each employee
    all_supervisors = set()
    for a, b in supervisors:
        all_supervisors.add(a)
        all_supervisors.add(b)
    direct_supervisors = set()
    for a, b in supervisors:
        direct_supervisors.add(a)
    indirect_supervisors = all_supervisors - direct_supervisors

    # find all the jokes told by the direct and indirect supervisors
    direct_supervisor_jokes = set()
    for a in direct_supervisors:
        direct_supervisor_jokes.add(V[a-1])
    indirect_supervisor_jokes = set()
    for a in indirect_supervisors:
        indirect_supervisor_jokes.add(V[a-1])

    # find all the possible sets of jokes
    all_jokes = set()
    for a in direct_supervisor_jokes:
        for b in indirect_supervisor_jokes:
            if a != b:
                all_jokes.add((a, b))

    return len(all_jokes)

def f2(N, V, supervisors):
    # find all the direct and indirect supervisors of each employee
    all_supervisors = set()
    for a, b in supervisors:
        all_supervisors.add(a)
        all_supervisors.add(b)
    direct_supervisors = set()
    for a, b in supervisors:
        direct_supervisors.add(a)
    indirect_supervisors = all_supervisors - direct_supervisors

    # find all the jokes told by the direct and indirect supervisors
    direct_supervisor_jokes = set()
    for a in direct_supervisors:
        direct_supervisor_jokes.add(V[a-1])
    indirect_supervisor_jokes = set()
    for a in indirect_supervisors:
        indirect_supervisor_jokes.add(V[a-1])

    # find all the possible sets of jokes
    all_jokes = set()
    for a in direct_supervisor_jokes:
        for b in indirect_supervisor_jokes:
            if a != b:
                all_jokes.add((a, b))

    # find the number of sets of jokes that form consecutive numbers
    consecutive_jokes = 0
    for a, b in all_jokes:
        if b-a == 1:
            consecutive_jokes += 1

    return consecutive_jokes

if __name__ == '__main__':
    N, V, supervisors = read_input()
    print(f2(N, V, supervisors))

