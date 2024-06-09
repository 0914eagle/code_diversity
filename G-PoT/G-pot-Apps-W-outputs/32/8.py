
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    sum_to_index = {}
    for i in range(n + 1):
        if prefix_sum[i] in sum_to_index:
            subset_size = i - sum_to_index[prefix_sum[i]]
            subset_indices = list(range(sum_to_index[prefix_sum[i]] + 1, i + 1))
            print(subset_size)
            print(*subset_indices)
            break
        sum_to_index[prefix_sum[i]] = i
