
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

sums = []
for a in A:
    for b in B:
        for c in C:
            sums.append(a + b + c)

sums.sort(reverse=True)
for i in range(K):
    print(sums[i])
