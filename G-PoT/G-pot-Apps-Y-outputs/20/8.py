
# Read input
N, Q = map(int, input().split())
S = input().strip()
queries = [list(map(int, input().split())) for _ in range(Q)]

# Count occurrences of AC in the prefix sum array
prefix_sum = [0]
for i in range(1, N):
    prefix_sum.append(prefix_sum[i-1] + (1 if S[i-1:i+1] == 'AC' else 0))

# Answer queries
for query in queries:
    l, r = query
    print(prefix_sum[r-1] - prefix_sum[l-1])

