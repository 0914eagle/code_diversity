
def solve_query(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == s[i-1]:
            count += 1
    return count

def solve_queries(s, queries):
    results = []
    for query in queries:
        l, r = query
        results.append(solve_query(s, l, r))
    return results

def main():
    s = input()
    m = int(input())
    queries = []
    for i in range(m):
        queries.append(list(map(int, input().split())))
    results = solve_queries(s, queries)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()

