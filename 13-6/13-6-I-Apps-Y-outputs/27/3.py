
def is_achievable(M, N, C, A, X):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money = 0
    
    # Initialize the understanding levels of the algorithms
    understanding_levels = [0] * M
    
    # Sort the books by their cost in descending order
    sorted_books = sorted(range(N), key=lambda i: C[i])
    
    # Iterate through the books and try to buy them
    for i in sorted_books:
        # Check if buying the current book will increase the understanding levels of all the algorithms to X or higher
        if all(understanding_levels[j] + A[i, j] >= X for j in range(M)):
            # If it will, add the cost of the current book to the minimum amount of money needed to achieve the objective
            min_money += C[i]
            # Update the understanding levels of the algorithms based on the current book
            for j in range(M):
                understanding_levels[j] += A[i, j]
    
    # Check if the minimum amount of money needed to achieve the objective is greater than or equal to the total cost of all the books
    if min_money >= sum(C):
        return True
    else:
        return False

def main():
    M, N, C, A, X = map(int, input().split())
    C = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(is_achievable(M, N, C, A, X))

if __name__ == '__main__':
    main()

