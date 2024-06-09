
n = int(input())
visitors = []
for _ in range(n):
    h, m = map(int, input().split())
    visitors.append(h * 60 + m)

visitors.sort()
cash_count = 0
for i in range(n):
    if cash_count == 0 or visitors[i] - visitors[i-1] > 15:
        cash_count += 1

print(cash_count)
