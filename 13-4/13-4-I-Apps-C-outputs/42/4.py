
def f1(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    # Initialize the ranking and the number of distinct ranks
    ranking = [1] * N
    num_distinct_ranks = 1

    for i in range(N):
        # Check if the current assistant is better than the previous one
        if a[i] + K < a[i-1] or b[i] + K < b[i-1]:
            # If so, give it a new rank
            ranking[i] = num_distinct_ranks + 1
            num_distinct_ranks += 1

    return num_distinct_ranks

def f2(N, K, a, b):
    # Sort the measurements in descending order
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    # Initialize the ranking and the number of distinct ranks
    ranking = [1] * N
    num_distinct_ranks = 1

    for i in range(N):
        # Check if the current assistant is better than the previous one
        if a[i] + K < a[i-1] or b[i] + K < b[i-1]:
            # If so, give it a new rank
            ranking[i] = num_distinct_ranks + 1
            num_distinct_ranks += 1

    return ranking

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(N, K, a, b))
    print(f2(N, K, a, b))

