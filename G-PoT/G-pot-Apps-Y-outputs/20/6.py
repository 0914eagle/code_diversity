
# Read input
N, Q = map(int, input().split())
S = input().strip()
queries = [list(map(int, input().split())) for _ in range(Q)]

# Count occurrences of "AC" in the string S
ac_count = [0] * (N + 1)
for i in range(1, N):
    ac_count[i] = ac_count[i-1] + (1 if S[i-1:i+1] == "AC" else 0)

# Process queries
for query in queries:
    l, r = query
    print(ac_count[r-1] - ac_count[l-1])
