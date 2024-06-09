
def f1(N, K, book):
    # find the largest committee with at least one member who disagrees with at least K other members
    max_committee = 0
    for i in range(N):
        # count the number of members who disagree with the ith member
        num_disagreements = 0
        for j in range(N):
            if j != i and book[i][j] == 1:
                num_disagreements += 1
        if num_disagreements >= K:
            max_committee = max(max_committee, num_disagreements + 1)
    return max_committee

def f2(N, K, book):
    # find the largest committee with at most K members
    max_committee = 0
    for i in range(1, N+1):
        for subset in itertools.combinations(range(N), i):
            num_disagreements = 0
            for j in subset:
                for k in subset:
                    if j != k and book[j][k] == 1:
                        num_disagreements += 1
            if num_disagreements <= K:
                max_committee = max(max_committee, len(subset))
    return max_committee

def main():
    N, K = map(int, input().split())
    book = []
    for i in range(N):
        book.append(list(map(int, input().split())))
    print(f2(N, K, book))

if __name__ == '__main__':
    main()

