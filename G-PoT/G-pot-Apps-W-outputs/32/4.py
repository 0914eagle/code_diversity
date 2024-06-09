
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    zero_sum_indices = []
    pos_indices = []
    neg_indices = []

    for i in range(n):
        if a[i] == 0:
            zero_sum_indices.append(i)
        elif a[i] > 0:
            pos_indices.append(i)
        else:
            neg_indices.append(i)

    if len(zero_sum_indices) > 0:
        print(1)
        print(zero_sum_indices[0] + 1)
    else:
        print(len(neg_indices) + 1)
        print(*neg_indices[::-1], *pos_indices)
