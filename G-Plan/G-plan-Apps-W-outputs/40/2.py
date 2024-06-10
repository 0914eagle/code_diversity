
def calculate_sum(a, c):
    n = len(a)
    a.sort()
    sum_values = 0
    for i in range(n - n // c):
        sum_values += a[i]
    return sum_values

def find_smallest_sum(n, c, a):
    partitions = []
    for i in range(1, n):
        partitions.append((a[:i], a[i:]))
    min_sum = float('inf')
    for p1, p2 in partitions:
        sum_values = calculate_sum(p1, c) + calculate_sum(p2, c)
        min_sum = min(min_sum, sum_values)
    return min_sum

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    result = find_smallest_sum(n, c, a)
    print(result)
