
def max_prettiness_contest(queries):
    def max_prettiness_single_query(n, prettiness):
        max_prettiness = 0
        for i in range(n):
            for j in range(i+1, n):
                if prettiness[j] % prettiness[i] != 0 and prettiness[i] % prettiness[j] != 0:
                    max_prettiness = max(max_prettiness, prettiness[i] + prettiness[j])
                for k in range(j+1, n):
                    if prettiness[k] % prettiness[i] != 0 and prettiness[i] % prettiness[k] != 0 and prettiness[k] % prettiness[j] != 0 and prettiness[j] % prettiness[k] != 0:
                        max_prettiness = max(max_prettiness, prettiness[i] + prettiness[j] + prettiness[k])
        return max_prettiness

    results = []
    for query in queries:
        n, prettiness = query
        results.append(max_prettiness_single_query(n, prettiness))
    return results

if __name__ == "__main__":
    q = int(input())
    queries = []
    for _ in range(q):
        n = int(input())
        prettiness = list(map(int, input().split()))
        queries.append((n, prettiness))
    
    results = max_prettiness_contest(queries)
    for result in results:
        print(result)
