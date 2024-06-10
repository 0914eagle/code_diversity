
def read_input():
    N, M, Q = map(int, input().split())
    queries = []
    for i in range(Q):
        query = input().split()
        queries.append(query)
    return N, M, Q, queries

def rotate_teachers(teachers, classes, x, K, p):
    for i in range(K):
        teachers[p[i] - 1] = classes[(x + i) % M]
    return teachers

def get_class(teachers, x, d):
    return teachers[(d - 1) % len(teachers)]

def solve(N, M, Q, queries):
    classes = list(range(1, N + 1))
    teachers = list(range(1, N + 1))
    for query in queries:
        if query[0] == "0":
            K = int(query[1])
            x = int(query[2])
            p = list(map(int, query[3:]))
            teachers = rotate_teachers(teachers, classes, x, K, p)
        else:
            d = int(query[1])
            x = int(query[2])
            print(get_class(teachers, x, d))

if __name__ == '__main__':
    N, M, Q, queries = read_input()
    solve(N, M, Q, queries)

