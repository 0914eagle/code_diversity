
def f1(n, m, a, b, x):
    # Initialize a 2D array to store the values of c
    c = [[0] * (m+1) for _ in range(n+1)]
    
    # Calculate the values of c
    for i in range(1, n+1):
        for j in range(1, m+1):
            c[i][j] = a[i-1] * b[j-1]
    
    # Initialize a variable to store the maximum area
    max_area = 0
    
    # Iterate over all possible areas
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i, n+1):
                for l in range(j, m+1):
                    # Calculate the sum of the elements in the current subrectangle
                    sum_elements = sum(sum(c[i:k+1], []))
                    # If the sum is less than or equal to x, update the maximum area
                    if sum_elements <= x:
                        max_area = max(max_area, (k-i+1) * (l-j+1))
    
    # Return the maximum area
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

