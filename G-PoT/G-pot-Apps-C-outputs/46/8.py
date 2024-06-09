
n = int(input())
array = list(map(int, input().split()))

neg_count = 0
total_sum = sum(abs(x) for x in array)

for x in array:
    if x < 0:
        neg_count += 1

if neg_count % 2 == 1:
    total_sum -= 2 * min(abs(x) for x in array)

print(total_sum)
