
N = int(input())
array = [int(input()) for _ in range(N)]

total_sum = 0
for i in range(N):
    for j in range(i, N):
        sub_array = array[i:j+1]
        min_val = min(sub_array)
        max_val = max(sub_array)
        length = len(sub_array)
        total_sum += min_val * max_val * length

last_nine_digits = total_sum % (10**9)
print(last_nine_digits)
