
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def get_max_hangout_days(N, M, A):
    # Sort the assignments by their deadlines
    A.sort()
    
    # Initialize the maximum number of hangout days
    max_hangout_days = 0
    
    # Iterate over the assignments
    for i in range(M):
        # Calculate the number of days Takahashi can hang out before the current assignment
        hangout_days = N - sum(A[:i])
        
        # Update the maximum number of hangout days
        max_hangout_days = max(max_hangout_days, hangout_days)
    
    return max_hangout_days

def main():
    N, M, A = get_input()
    print(get_max_hangout_days(N, M, A))

if __name__ == '__main__':
    main()

