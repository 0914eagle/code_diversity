
def f1(n, m, a, b, x):
    # Initialize a 2D array to store the values of c
    c = [[0] * m for _ in range(n)]
    
    # Calculate the values of c
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i] * b[j]
    
    # Initialize a variable to store the maximum area
    max_area = 0
    
    # Iterate over all possible subrectangles
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    # Calculate the sum of the elements in the current subrectangle
                    sum_elements = sum(sum(c[i:k+1], []))
                    
                    # If the sum is less than or equal to x, update the maximum area
                    if sum_elements <= x:
                        max_area = max(max_area, (k-i+1) * (l-j+1))
    
    return max_area

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = int(input())
    
    print(f1(n, m, a, b, x))

