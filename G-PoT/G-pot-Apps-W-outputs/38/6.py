
t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    strengths = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (-1)**(i % 2) * strengths[i - 1]

    for _ in range(q):
        l, r = map(int, input().split())
        diff = strengths[r - 1] - strengths[l - 1]
        if (r - l) % 2 == 0:
            diff *= -1
        prefix_sum[l - 1] += diff
        prefix_sum[r] -= diff

    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    print(*prefix_sum[1:])
