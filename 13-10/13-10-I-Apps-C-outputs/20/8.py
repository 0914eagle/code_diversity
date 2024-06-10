
def recursive_relation(A, B):
    if A == B:
        return 1
    else:
        return recursive_relation(A, B-1) + recursive_relation(B-1, B)

def solve(Q, queries):
    result = []
    for query in queries:
        A, B = query
        result.append(recursive_relation(A, B))
    return result

if __name__ == '__main__':
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    result = solve(Q, queries)
    for i in result:
        print(i)

