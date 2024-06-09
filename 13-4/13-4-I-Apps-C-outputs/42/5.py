
def f1(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    # Initialize the ranking and the number of distinct ranks
    ranking = [0] * N
    distinct_ranks = 1
    
    # Loop through each assistant and assign a ranking
    for i in range(N):
        # If the current assistant has a better quality than the previous one, assign a new ranking
        if a[i] + K < a[i-1] or b[i] + K < b[i-1]:
            ranking[i] = distinct_ranks
            distinct_ranks += 1
        # Otherwise, assign the same ranking as the previous assistant
        else:
            ranking[i] = ranking[i-1]
    
    return distinct_ranks

def f2(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    # Initialize the ranking and the number of distinct ranks
    ranking = [0] * N
    distinct_ranks = 1
    
    # Loop through each assistant and assign a ranking
    for i in range(N):
        # If the current assistant has a better quality than the previous one, assign a new ranking
        if a[i] + K < a[i-1] or b[i] + K < b[i-1]:
            ranking[i] = distinct_ranks
            distinct_ranks += 1
        # Otherwise, assign the same ranking as the previous assistant
        else:
            ranking[i] = ranking[i-1]
    
    return ranking

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(N, K, a, b))
    print(f2(N, K, a, b))

