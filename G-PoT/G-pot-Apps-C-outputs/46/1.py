
n = int(input())
arr = list(map(int, input().split()))

neg_count = sum(1 for num in arr if num < 0)
if n % 2 == 1:
    neg_count += 1

arr = [abs(num) for num in arr]
arr.sort()

if neg_count % 2 == 1:
    arr[0] *= -1

print(sum(arr))
