
def get_segments(query):
    l1, r1, l2, r2 = map(int, query.split())
    return [l1, r1, l2, r2]

def find_intersection(segments):
    l1, r1, l2, r2 = segments
    if l1 <= l2:
        return l2
    else:
        return l1

def find_non_intersection(segments):
    l1, r1, l2, r2 = segments
    if l1 <= l2:
        return r2
    else:
        return r1

def solve(queries):
    results = []
    for query in queries:
        segments = get_segments(query)
        intersection = find_intersection(segments)
        non_intersection = find_non_intersection(segments)
        results.append([intersection, non_intersection])
    return results

if __name__ == '__main__':
    q = int(input())
    queries = [input() for _ in range(q)]
    results = solve(queries)
    for result in results:
        print(*result)

