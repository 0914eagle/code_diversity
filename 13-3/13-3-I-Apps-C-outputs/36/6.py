
def f1(n, m, a, b, x):
    # Initialize a matrix to store the product of a and b
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i] * b[j]
    
    # Initialize a variable to store the maximum area
    max_area = 0
    
    # Iterate over all possible starting points
    for i in range(n):
        for j in range(m):
            # Initialize a variable to store the current area
            curr_area = 0
            # Iterate over all possible sizes
            for k in range(n-i+1):
                for l in range(m-j+1):
                    # Calculate the current sum
                    curr_sum = sum(sum(c[i+k-1][j+l-1:j+l]) for k in range(k+1))
                    # If the current sum is less than or equal to x, update the maximum area
                    if curr_sum <= x:
                        max_area = max(max_area, k*l)
    
    return max_area

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = int(input())
    print(f1(n, m, a, b, x))

