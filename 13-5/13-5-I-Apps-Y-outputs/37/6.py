
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def solve(N, M, A):
    # Sort the assignments by deadline
    A.sort()
    
    # Initialize the maximum number of days Takahashi can hang out
    max_days = 0
    
    # Iterate over the assignments
    for i in range(M):
        # Calculate the number of days Takahashi has left after completing the current assignment
        days_left = N - A[i]
        
        # If Takahashi has enough days left to complete all the remaining assignments, update the maximum number of days he can hang out
        if days_left >= sum(A[i+1:]):
            max_days = max(max_days, days_left)
    
    # If Takahashi cannot complete all the assignments during the vacation, return -1
    if max_days == 0:
        return -1
    
    # Otherwise, return the maximum number of days Takahashi can hang out
    return max_days

def main():
    N, M, A = get_input()
    print(solve(N, M, A))

if __name__ == '__main__':
    main()

