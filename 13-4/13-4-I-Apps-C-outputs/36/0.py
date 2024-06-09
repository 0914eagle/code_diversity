
def get_input():
    N = int(input())
    V = list(map(int, input().split()))
    direct_supervisors = []
    for _ in range(N-1):
        direct_supervisors.append(list(map(int, input().split())))
    return N, V, direct_supervisors

def get_supervisors(direct_supervisors, N):
    supervisors = [[] for _ in range(N+1)]
    for supervisor, employee in direct_supervisors:
        supervisors[employee].append(supervisor)
    for i in range(2, N+1):
        for j in range(1, i):
            if i in supervisors[j]:
                supervisors[i].extend(supervisors[j])
    return supervisors

def get_jokes(V, supervisors, N):
    jokes = set()
    for i in range(1, N+1):
        if not supervisors[i]:
            continue
        for j in supervisors[i]:
            if V[i] != V[j]:
                jokes.add((V[i], V[j]))
    return jokes

def count_consecutive_jokes(jokes, N):
    count = 0
    for i in range(1, N+1):
        if not supervisors[i]:
            continue
        for j in supervisors[i]:
            if V[i] != V[j] and (V[i]-V[j])%N == 1:
                count += 1
    return count

def main():
    N, V, direct_supervisors = get_input()
    supervisors = get_supervisors(direct_supervisors, N)
    jokes = get_jokes(V, supervisors, N)
    count = count_consecutive_jokes(jokes, N)
    print(count)

if __name__ == '__main__':
    main()

