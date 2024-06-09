
def f1(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    # Initialize the ranking and the number of distinct ranks
    ranking = [1] * N
    num_ranks = 1
    
    # Iterate through the measurements and assign ranks
    for i in range(N):
        for j in range(i+1, N):
            if a[i] + K < a[j] or b[i] + K < b[j]:
                ranking[j] = ranking[i]
    
    # Count the number of distinct ranks
    for i in range(N):
        if ranking[i] == i + 1:
            num_ranks += 1
    
    return num_ranks

def f2(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    # Initialize the ranking and the number of distinct ranks
    ranking = [1] * N
    num_ranks = 1
    
    # Iterate through the measurements and assign ranks
    for i in range(N):
        for j in range(i+1, N):
            if a[i] + K < a[j] or b[i] + K < b[j]:
                ranking[j] = ranking[i]
    
    # Count the number of distinct ranks
    for i in range(N):
        if ranking[i] == i + 1:
            num_ranks += 1
    
    return num_ranks

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(N, K, a, b))
    print(f2(N, K, a, b))

