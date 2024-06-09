
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

result = [(p[i] + q[i]) % n for i in range(n)]
print(*result)
