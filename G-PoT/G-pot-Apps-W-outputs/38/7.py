
t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    strengths = list(map(int, input().split()))
    swaps = [list(map(int, input().split())) for _ in range(q)]

    prefix_sum = [0]
    for i in range(1, n+1):
        prefix_sum.append(prefix_sum[-1] + (-1)**(i) * strengths[i-1])

    for l, r in swaps:
        diff = strengths[r-1] - strengths[l-1]
        if (r-l) % 2 == 0:
            diff *= -1
        print(prefix_sum[l-1] + prefix_sum[r] + diff)

    print(prefix_sum[-1])
