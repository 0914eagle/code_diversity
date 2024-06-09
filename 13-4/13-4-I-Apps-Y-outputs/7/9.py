
def f1(N, M, C, B, A):
    # Calculate the sum of the products of the coefficients and the input values
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    # Check if the sum is greater than the constant
    if sum > C:
        return 1
    else:
        return 0

def f2(N, M, C, B, A):
    # Calculate the sum of the products of the coefficients and the input values
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    # Check if the sum is greater than the constant
    if sum > C:
        return 1
    else:
        return 0

if __name__ == '__main__':
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    # Calculate the number of codes that correctly solve the problem
    count = 0
    for i in range(N):
        count += f1(N, M, C, B, A[i])
    print(count)

