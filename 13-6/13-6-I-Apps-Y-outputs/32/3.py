
def find_intersection(l1, r1, l2, r2):
    if l1 <= l2:
        return l1, l2
    elif l1 <= r2:
        return l1, r2
    elif l2 <= r1:
        return l2, r1
    else:
        return l2, l1

def solve(queries):
    result = []
    for query in queries:
        l1, r1, l2, r2 = query
        a, b = find_intersection(l1, r1, l2, r2)
        result.append([a, b])
    return result

if __name__ == '__main__':
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    result = solve(queries)
    for i, query in enumerate(result):
        print(f"Case {i+1}: {query[0]} {query[1]}")

