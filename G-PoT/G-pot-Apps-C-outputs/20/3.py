
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

total_sum = 0
for i in range(N):
    for j in range(i, N):
        subarray = array[i:j+1]
        min_val = min(subarray)
        max_val = max(subarray)
        length = len(subarray)
        total_sum += min_val * max_val * length

last_nine_digits = total_sum % 10**9
print(last_nine_digits)
