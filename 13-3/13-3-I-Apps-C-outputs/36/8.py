
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
            # Iterate over all possible lengths
            for k in range(n - i + 1):
                # Check if the current area is less than or equal to x
                if curr_area <= x:
                    # Add the current area to the maximum area
                    max_area = max(max_area, curr_area)
                # Update the current area
                curr_area += c[i + k - 1][j + k - 1] - c[i + k - 1][j - 1] - c[i - 1][j + k - 1] + c[i - 1][j - 1]
    
    # Return the maximum area
    return max_area

def f2(n, m, a, b, x):
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
            # Iterate over all possible lengths
            for k in range(n - i + 1):
                # Check if the current area is less than or equal to x
                if curr_area <= x:
                    # Add the current area to the maximum area
                    max_area = max(max_area, curr_area)
                # Update the current area
                curr_area += c[i + k - 1][j + k - 1] - c[i + k - 1][j - 1] - c[i - 1][j + k - 1] + c[i - 1][j - 1]
    
    # Return the maximum area
    return max_area

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = int(input())
    print(f1(n, m, a, b, x))
    print(f2(n, m, a, b, x))

