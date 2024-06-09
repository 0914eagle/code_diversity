
def f1(N, M, C, B, A):
    # Calculate the sum of the products of the coefficients and the input values
    sum = 0
    for i in range(N):
        sum += A[i] @ B + C
    
    # Return the number of codes that correctly solve the problem
    return sum

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(f1(N, M, C, B, A))

