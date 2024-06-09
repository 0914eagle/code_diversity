
t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    strengths = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + strengths[i - 1]

    for _ in range(q):
        l, r = map(int, input().split())
        diff = strengths[l - 1] - strengths[r - 1]
        if diff > 0:
            diff = -diff
        print(prefix_sum[r] - prefix_sum[l - 1] + diff)

    print(prefix_sum[n])
