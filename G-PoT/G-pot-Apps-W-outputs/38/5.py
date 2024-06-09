
t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    strengths = list(map(int, input().split()))
    swaps = [list(map(int, input().split())) for _ in range(q)]

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (-1) ** (i % 2) * strengths[i - 1]

    for l, r in swaps:
        diff = strengths[r - 1] - strengths[l - 1]
        if (r - l) % 2 == 0:
            diff *= -1
        for i in range(r, n + 1):
            prefix_sum[i] += diff

        result = str(prefix_sum[n])
        for i in range(q):
            result += "\n" + str(prefix_sum[n] - prefix_sum[i])

        print(result)
