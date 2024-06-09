
n = int(input())
for _ in range(n):
    k, x = map(int, input().split())
    result = (k - 1) * 9 + x
    print(result)
