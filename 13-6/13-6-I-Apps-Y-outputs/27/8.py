
def is_achievable(M, N, C, A, X):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money = 0
    
    # Initialize the understanding levels of the algorithms
    understanding_levels = [0] * M
    
    # Sort the books by their cost in descending order
    sorted_books = sorted(range(N), key=lambda i: C[i])
    
    # Iterate through the books in descending order of cost
    for i in sorted_books:
        # Check if buying the current book will increase the understanding levels of any algorithms
        for j in range(M):
            if understanding_levels[j] < X and A[i, j] > 0:
                # Increase the understanding level of the algorithm
                understanding_levels[j] += A[i, j]
                
                # Check if all the algorithms have reached the required understanding level
                if all(understanding_level >= X for understanding_level in understanding_levels):
                    # Return the minimum amount of money needed to achieve the objective
                    return min_money + C[i]
                break
        else:
            # If none of the algorithms can be increased, increase the minimum amount of money needed
            min_money += C[i]
    
    # If all the algorithms have not been achieved, return -1
    return -1

def main():
    M, N, C, A, X = map(int, input().split())
    C = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for _ in range(N)]
    print(is_achievable(M, N, C, A, X))

if __name__ == '__main__':
    main()

