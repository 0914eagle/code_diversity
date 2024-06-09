
# Read input
N, Q = map(int, input().split())
S = input().strip()
queries = [list(map(int, input().split())) for _ in range(Q)]

# Preprocess to count occurrences of "AC" in each prefix of the string
ac_count = [0]
for i in range(1, N):
    ac_count.append(ac_count[i-1] + (S[i-1:i+1] == 'AC'))

# Process queries
for query in queries:
    l, r = query
    print(ac_count[r-1] - ac_count[l-1])
