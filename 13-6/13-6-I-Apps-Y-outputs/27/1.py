
def is_achievable(M, N, C, A, X):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money = 0
    
    # Initialize the understanding levels of the algorithms
    understanding_levels = [0] * M
    
    # Sort the books by their cost in descending order
    sorted_books = sorted(range(N), key=lambda i: C[i])
    
    # Iterate through the books in descending order of cost
    for i in sorted_books:
        # Check if buying the current book will increase the understanding levels of all the algorithms to X or higher
        if all(understanding_levels[j] + A[i, j] >= X for j in range(M)):
            # If so, add the cost of the current book to the minimum amount of money needed to achieve the objective
            min_money += C[i]
            # Increase the understanding levels of the algorithms by the amount specified in the current book
            for j in range(M):
                understanding_levels[j] += A[i, j]
    
    # Return True if the minimum amount of money needed to achieve the objective is non-negative, and False otherwise
    return min_money >= 0

def find_min_money(M, N, C, A, X):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money = 0
    
    # Initialize the understanding levels of the algorithms
    understanding_levels = [0] * M
    
    # Sort the books by their cost in descending order
    sorted_books = sorted(range(N), key=lambda i: C[i])
    
    # Iterate through the books in descending order of cost
    for i in sorted_books:
        # Check if buying the current book will increase the understanding levels of all the algorithms to X or higher
        if all(understanding_levels[j] + A[i, j] >= X for j in range(M)):
            # If so, add the cost of the current book to the minimum amount of money needed to achieve the objective
            min_money += C[i]
            # Increase the understanding levels of the algorithms by the amount specified in the current book
            for j in range(M):
                understanding_levels[j] += A[i, j]
    
    # Return the minimum amount of money needed to achieve the objective
    return min_money

if __name__ == '__main__':
    M, N, C, A, X = map(int, input().split())
    C = [int(i) for i in input().split()]
    A = [[int(i) for i in input().split()] for _ in range(N)]
    print(find_min_money(M, N, C, A, X))

