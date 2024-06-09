
def get_optimal_subsequence(a, k, pos):
    # Find the optimal subsequence of length k
    optimal_subsequence = []
    for i in range(k):
        optimal_subsequence.append(max(a[i:i+k]))
    
    # Return the value at the given position in the optimal subsequence
    return optimal_subsequence[pos-1]


n = int(input())
a = list(map(int, input().split()))
m = int(input())

for i in range(m):
    k, pos = map(int, input().split())
    print(get_optimal_subsequence(a, k, pos))



