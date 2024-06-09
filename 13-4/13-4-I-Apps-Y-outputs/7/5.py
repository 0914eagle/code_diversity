
def f1(N, M, C, B, A):
    # Calculate the sum of products of B and A
    sum_products = sum([b * a for b, a in zip(B, A)])
    # Check if the sum is greater than C
    if sum_products > C:
        return 1
    else:
        return 0

def f2(N, M, C, B, A):
    # Initialize a counter for the number of correct codes
    count = 0
    # Loop through each code
    for i in range(N):
        # Calculate the sum of products of B and A for the current code
        sum_products = sum([b * a for b, a in zip(B, A[i])])
        # Check if the sum is greater than C
        if sum_products > C:
            count += 1
    # Return the number of correct codes
    return count

if __name__ == '__main__':
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(f2(N, M, C, B, A))

