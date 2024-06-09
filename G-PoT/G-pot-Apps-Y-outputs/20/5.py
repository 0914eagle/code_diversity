
# Read input
N, Q = map(int, input().split())
S = input().strip()
queries = [list(map(int, input().split())) for _ in range(Q)]

# Preprocess the string to count occurrences of AC
ac_count = [0] * N
for i in range(1, N):
    ac_count[i] = ac_count[i-1] + (S[i-1:i+1] == 'AC')

# Answer the queries
for query in queries:
    l, r = query
    print(ac_count[r-1] - ac_count[l-1])
