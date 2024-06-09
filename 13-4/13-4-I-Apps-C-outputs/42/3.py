
def f1(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    # Initialize the ranking with the highest quality
    ranking = [1] * N

    # Loop through each assistant and compare their measurements
    for i in range(N):
        for j in range(i+1, N):
            if a[i] + K < a[j] or b[i] + K < b[j]:
                ranking[j] = ranking[i]

    # Return the number of distinct ranks
    return len(set(ranking))

def f2(N, K, a, b):
    # Initialize the ranking with the highest quality
    ranking = [1] * N

    # Loop through each assistant and compare their measurements
    for i in range(N):
        for j in range(i+1, N):
            if a[i] + K < a[j] or b[i] + K < b[j]:
                ranking[j] = ranking[i]

    # Return the number of distinct ranks
    return len(set(ranking))

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(N, K, a, b))

