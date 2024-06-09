
def get_intersection(l1, r1, l2, r2):
    if l1 <= l2:
        return max(l1, l2), min(r1, r2)
    else:
        return max(l2, l1), min(r2, r1)

def solve(queries):
    result = []
    for query in queries:
        l1, r1, l2, r2 = map(int, query.split())
        a, b = get_intersection(l1, r1, l2, r2)
        result.append([a, b])
    return result

if __name__ == '__main__':
    q = int(input())
    queries = [input() for _ in range(q)]
    result = solve(queries)
    for a, b in result:
        print(a, b)

