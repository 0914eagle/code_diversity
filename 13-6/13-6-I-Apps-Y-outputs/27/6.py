
def is_achievable(C, A, M, X):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money = 0
    
    # Initialize the understanding levels of all the algorithms to 0
    understanding_levels = [0] * M
    
    # Sort the books by their cost in ascending order
    sorted_books = sorted(enumerate(C), key=lambda x: x[1])
    
    # Iterate through the books and buy them if it will increase the understanding level of at least one algorithm to X or higher
    for i, (book_index, cost) in enumerate(sorted_books):
        # Check if buying the current book will increase the understanding level of at least one algorithm to X or higher
        if any(understanding_levels[j] + A[book_index][j] >= X for j in range(M)):
            # Increase the understanding levels of all the algorithms that will be increased by buying the current book
            for j in range(M):
                if understanding_levels[j] + A[book_index][j] >= X:
                    understanding_levels[j] += A[book_index][j]
            
            # Add the cost of the current book to the minimum amount of money needed to achieve the objective
            min_money += cost
    
    # Check if all the understanding levels are X or higher
    if all(understanding_level >= X for understanding_level in understanding_levels):
        return True, min_money
    else:
        return False, -1

def main():
    # Read the input
    M, X = map(int, input().split())
    C = list(map(int, input().split()))
    A = []
    for i in range(len(C)):
        A.append(list(map(int, input().split())))
    
    # Solve the problem
    result = is_achievable(C, A, M, X)
    
    # Print the result
    if result[0]:
        print("Yes")
        print(result[1])
    else:
        print("No")

if __name__ == '__main__':
    main()

