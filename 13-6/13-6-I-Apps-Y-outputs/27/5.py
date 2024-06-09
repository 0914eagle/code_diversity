
def is_achievable(M, N, C, A, X):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money = 0
    
    # Initialize the understanding levels of the algorithms
    levels = [0] * M
    
    # Sort the books by their cost in ascending order
    sorted_books = sorted(range(N), key=lambda i: C[i])
    
    # Iterate through the books in ascending order of cost
    for i in sorted_books:
        # Check if the current book can increase the understanding level of any algorithm to X or higher
        for j in range(M):
            if levels[j] + A[i, j] >= X:
                # If so, buy the book and update the understanding levels
                levels[j] += A[i, j]
                min_money += C[i]
                break
    
    # Check if all the understanding levels are at least X
    if all(level >= X for level in levels):
        return min_money
    else:
        return -1

def main():
    M, N, C, A, X = map(int, input().split())
    C = list(map(int, input().split()))
    A = [[int(i) for i in input().split()] for _ in range(N)]
    print(is_achievable(M, N, C, A, X))

if __name__ == '__main__':
    main()

