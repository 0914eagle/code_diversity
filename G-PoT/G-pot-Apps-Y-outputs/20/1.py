
# Read input
N, Q = map(int, input().split())
S = input().strip()
queries = [list(map(int, input().split())) for _ in range(Q)]

# Count occurrences of "AC" in the substring
def count_AC(substring):
    count = 0
    for i in range(len(substring) - 1):
        if substring[i:i+2] == "AC":
            count += 1
    return count

# Process queries
for query in queries:
    l, r = query
    substring = S[l-1:r]
    print(count_AC(substring))
