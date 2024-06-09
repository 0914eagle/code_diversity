
N, Q = map(int, input().split())
S = input().strip()
occurrences = [0] * (N + 1)

for i in range(1, N):
    occurrences[i] = occurrences[i-1] + (1 if S[i-1:i+1] == 'AC' else 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(occurrences[r-1] - occurrences[l-1])

