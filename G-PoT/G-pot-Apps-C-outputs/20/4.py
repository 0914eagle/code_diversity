
N = int(input())
array = [int(input()) for _ in range(N)]

total_sum = 0
for i in range(N):
    min_val = array[i]
    max_val = array[i]
    for j in range(i, N):
        min_val = min(min_val, array[j])
        max_val = max(max_val, array[j])
        total_sum += min_val * max_val * (j - i + 1)

print(total_sum % 10**9)
