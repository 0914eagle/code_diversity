
N = int(input())
array = [int(input()) for _ in range(N)]

total_sum = 0
for i in range(N):
    for j in range(i, N):
        min_val = min(array[i:j+1])
        max_val = max(array[i:j+1])
        length = j - i + 1
        total_sum += min_val * max_val * length

print(total_sum % 10**9)
