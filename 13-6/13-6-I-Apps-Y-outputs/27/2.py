
def can_achieve(C, A, X):
    # Initialize the minimum amount of money needed to achieve the objective as infinity
    min_money = float('inf')
    
    # Initialize the current understanding level of each algorithm as 0
    current_level = [0] * len(A)
    
    # Sort the books by their prices in descending order
    sorted_books = sorted(range(len(C)), key=lambda i: C[i], reverse=True)
    
    # Iterate through the books in descending order of their prices
    for i in sorted_books:
        # Check if the current understanding level of each algorithm is less than or equal to X
        if all(current_level[j] <= X[j] for j in range(len(A))):
            # If all algorithms have been achieved, return the current minimum amount of money needed
            return min_money
        
        # Iterate through the algorithms and increase their understanding levels by the corresponding amount
        for j in range(len(A)):
            current_level[j] += A[i][j]
        
        # Update the minimum amount of money needed to achieve the objective
        min_money = min(min_money, C[i])
    
    # If the objective is not achievable, return -1
    return -1

def main():
    # Read the number of algorithms and the number of books
    M, N = map(int, input().split())
    
    # Read the prices of the books
    C = list(map(int, input().split()))
    
    # Read the increase in understanding levels for each algorithm for each book
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        A[i] = list(map(int, input().split()))
    
    # Read the minimum understanding levels of each algorithm to achieve
    X = list(map(int, input().split()))
    
    # Determine if the objective is achievable and find the minimum amount of money needed
    result = can_achieve(C, A, X)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

