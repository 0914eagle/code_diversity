
def smallest_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def final_value_after_operations(t, queries):
    results = []
    for n, k in queries:
        for _ in range(k):
            n += smallest_divisor(n)
        results.append(n)
    return results

if __name__ == '__main__':
    t = int(input())
    queries = [list(map(int, input().split())) for _ in range(t)]
    results = final_value_after_operations(t, queries)
    for result in results:
        print(result)
