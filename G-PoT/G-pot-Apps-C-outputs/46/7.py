
n = int(input())
array = list(map(int, input().split()))

neg_count = sum(1 for num in array if num < 0)
if neg_count % 2 == 0 or n == 1:
    print(sum(abs(num) for num in array))
else:
    min_abs = min(abs(num) for num in array)
    print(sum(abs(num) for num in array) - 2 * min_abs)
