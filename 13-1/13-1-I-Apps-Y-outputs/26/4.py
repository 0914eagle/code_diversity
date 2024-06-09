
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

distances = []
for i in range(n):
    for j in range(i+1, n):
        distances.append(abs(x[i] - x[j]) / abs(v[i] - v[j]))

print(sum(distances))

