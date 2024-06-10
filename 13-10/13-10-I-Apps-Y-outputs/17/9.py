
def get_lexicographically_smallest_permutations(P, Q):
    N = len(P)
    permutations = []
    for i in range(1, N+1):
        for perm in itertools.permutations(range(1, N+1), N):
            permutations.append(list(perm))
    
    P_index = permutations.index(P) + 1
    Q_index = permutations.index(Q) + 1
    
    return P_index, Q_index

def get_absolute_difference(P_index, Q_index):
    return abs(P_index - Q_index)

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P_index, Q_index = get_lexicographically_smallest_permutations(P, Q)
    print(get_absolute_difference(P_index, Q_index))

