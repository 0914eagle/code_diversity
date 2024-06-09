
def get_disagreements(politicians, book):
    disagreements = 0
    for i in range(len(politicians)):
        for j in range(i+1, len(politicians)):
            if politicians[i] in book[j] and politicians[j] in book[i]:
                disagreements += 1
    return disagreements

def get_largest_committee(politicians, book, k):
    for i in range(len(politicians), 0, -1):
        committee = politicians[:i]
        if get_disagreements(committee, book) >= k:
            return i
    return 0

def main():
    n, k = map(int, input().split())
    politicians = list(range(n))
    book = [set(map(int, input().split())) for _ in range(n)]
    print(get_largest_committee(politicians, book, k))

if __name__ == '__main__':
    main()

