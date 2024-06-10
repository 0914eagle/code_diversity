
def max_prettiness(queries):
    results = []
    for query in queries:
        n = query[0]
        prettiness_values = query[1]
        prettiness_values.sort(reverse=True)
        max_total_prettiness = 0

        for i in range(n):
            for j in range(i + 1, n):
                if prettiness_values[i] % prettiness_values[j] != 0:
                    for k in range(j + 1, n):
                        if prettiness_values[j] % prettiness_values[k] != 0 and prettiness_values[i] % prettiness_values[k] != 0:
                            total_prettiness = prettiness_values[i] + prettiness_values[j] + prettiness_values[k]
                            max_total_prettiness = max(max_total_prettiness, total_prettiness)

        results.append(max_total_prettiness)

    return results

if __name__ == "__main__":
    q = int(input())
    queries = []
    for _ in range(q):
        n = int(input())
        prettiness_values = list(map(int, input().split()))
        queries.append((n, prettiness_values))

    results = max_prettiness(queries)
    for result in results:
        print(result)
