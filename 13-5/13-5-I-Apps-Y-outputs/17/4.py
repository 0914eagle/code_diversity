
def get_min_mp(N, A, B, C, lengths):
    # Initialize variables
    min_mp = 0
    bamboos = lengths.copy()

    # Use Extension Magic
    while any(l < A for l in bamboos):
        min_mp += 1
        for i in range(N):
            if bamboos[i] < A:
                bamboos[i] += 1
                break

    # Use Shortening Magic
    while any(l >= B for l in bamboos):
        min_mp += 1
        for i in range(N):
            if bamboos[i] >= B:
                bamboos[i] -= 1
                break

    # Use Composition Magic
    while len(bamboos) > 1:
        min_mp += 10
        for i in range(N-1):
            for j in range(i+1, N):
                if bamboos[i] + bamboos[j] == C:
                    bamboos[i] = 0
                    bamboos[j] = 0
                    break

    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    lengths = list(map(int, input().split()))
    print(get_min_mp(N, A, B, C, lengths))

if __name__ == '__main__':
    main()

