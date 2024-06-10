
def get_number_of_appearances(interval):
    a, b = interval
    return b - a + 1

def solve(queries):
    results = []
    for query in queries:
        results.append(get_number_of_appearances(query))
    return results

if __name__ == '__main__':
    q = int(input())
    queries = []
    for i in range(q):
        a, b = map(int, input().split())
        queries.append((a, b))
    results = solve(queries)
    for result in results:
        print(result)

