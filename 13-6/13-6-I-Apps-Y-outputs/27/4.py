
def can_achieve_objective(M, N, C, A):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money_needed = 0
    
    # Initialize the understanding levels of the algorithms
    understanding_levels = [0] * M
    
    # Loop through each book
    for i in range(N):
        # Check if the book can be bought
        if min_money_needed + C[i] <= X:
            # Increase the understanding levels of the algorithms
            for j in range(M):
                understanding_levels[j] += A[i, j]
    
    # Check if the objective is achievable
    if all(understanding_level >= X for understanding_level in understanding_levels):
        return True
    else:
        return False

def get_minimum_money_needed(M, N, C, A):
    # Initialize the minimum amount of money needed to achieve the objective
    min_money_needed = 0
    
    # Initialize the understanding levels of the algorithms
    understanding_levels = [0] * M
    
    # Loop through each book
    for i in range(N):
        # Check if the book can be bought
        if min_money_needed + C[i] <= X:
            # Increase the understanding levels of the algorithms
            for j in range(M):
                understanding_levels[j] += A[i, j]
            # Update the minimum amount of money needed to achieve the objective
            min_money_needed += C[i]
    
    # Return the minimum amount of money needed to achieve the objective
    return min_money_needed

if __name__ == '__main__':
    M, N, X = map(int, input().split())
    C = list(map(int, input().split()))
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            A[i][j] = int(input())
    
    if can_achieve_objective(M, N, C, A):
        print(get_minimum_money_needed(M, N, C, A))
    else:
        print(-1)

