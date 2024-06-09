
n = int(input())
array = list(map(int, input().split()))

neg_count = sum(1 for num in array if num < 0)
if n % 2 == 1:
    print(sum(abs(num) for num in array) - 2 * min(abs(num) for num in array))
else:
    if neg_count % 2 == 0:
        print(sum(abs(num) for num in array))
    else:
        print(sum(abs(num) for num in array) - 2 * min(abs(num) for num in array))
