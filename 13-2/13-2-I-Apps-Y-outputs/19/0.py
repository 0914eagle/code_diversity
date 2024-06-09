
def f1(N, A):
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(N):
        num_orders *= (N - i)
    
    # Calculate the number of incorrect reports
    num_incorrect = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                num_incorrect += 1
    
    # Calculate the number of possible orders with incorrect reports
    num_orders_with_incorrect = num_orders - num_incorrect
    
    # Return the number of possible orders with correct reports
    return num_orders_with_incorrect % (10**9 + 7)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(f1(N, A))

