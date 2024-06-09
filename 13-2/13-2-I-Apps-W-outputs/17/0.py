
n = int(input())
prices = list(map(int, input().split()))
q = int(input())
m = [int(input()) for _ in range(q)]

result = []
for day in m:
    count = 0
    for i in range(n):
        if prices[i] <= day:
            count += 1
    result.append(count)

print(*result, sep='\n')

