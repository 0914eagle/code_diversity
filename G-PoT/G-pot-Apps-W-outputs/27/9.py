
n = int(input())
visitors = []
for _ in range(n):
    h, m = map(int, input().split())
    visitors.append(h * 60 + m)

visitors.sort()
cash_count = 1
max_cash_count = 1

for i in range(1, n):
    if visitors[i] == visitors[i-1]:
        cash_count += 1
    else:
        cash_count = 1
    max_cash_count = max(max_cash_count, cash_count)

print(max_cash_count)
