
def get_prettiness_sum(a, k):
    # Calculate the cumulative prettiness of the first k problems
    return sum(a[:k])

def get_best_prettiness_sum(a, k):
    # Find the maximum possible cumulative prettiness of the first k problems
    max_sum = 0
    for i in range(k):
        for j in range(i+1, k):
            if a[i] % a[j] == 0 or a[j] % a[i] == 0:
                continue
            sum = get_prettiness_sum(a, k)
            if sum > max_sum:
                max_sum = sum
    return max_sum

def solve(queries):
    for query in queries:
        n = int(query[0])
        a = list(map(int, query[1:]))
        print(get_best_prettiness_sum(a, n))

if __name__ == '__main__':
    q = int(input())
    queries = [input().split() for _ in range(q)]
    solve(queries)

