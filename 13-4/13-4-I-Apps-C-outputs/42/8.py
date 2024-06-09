
def f1(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    # Initialize the ranking dictionary
    ranking = {}
    
    # Loop through each assistant and assign a ranking
    for i in range(N):
        # Check if the current assistant is the best in terms of jokes or compliments
        if a[i] + K >= a[0] or b[i] + K >= b[0]:
            # Assign the current assistant the highest ranking
            ranking[i] = 1
        else:
            # Assign the current assistant the lowest ranking
            ranking[i] = N
    
    # Return the number of distinct ranks
    return len(set(ranking.values()))

def f2(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    
    # Initialize the ranking dictionary
    ranking = {}
    
    # Loop through each assistant and assign a ranking
    for i in range(N):
        # Check if the current assistant is the best in terms of jokes or compliments
        if a[i] + K >= a[0] or b[i] + K >= b[0]:
            # Assign the current assistant the highest ranking
            ranking[i] = 1
        else:
            # Assign the current assistant the lowest ranking
            ranking[i] = N
    
    # Return the number of distinct ranks
    return len(set(ranking.values()))

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(N, K, a, b))
    print(f2(N, K, a, b))

