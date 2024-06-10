
def find_minimum_positive_divisible_by_d(l, r, d):
    for i in range(l, r+1):
        if i % d == 0 and i not in range(l, r+1):
            return i
    return -1

def solve_queries(queries):
    for query in queries:
        l, r, d = query
        print(find_minimum_positive_divisible_by_d(l, r, d))

if __name__ == '__main__':
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    solve_queries(queries)

