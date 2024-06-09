
def f1(n, m, a, b, x):
    # Initialize a 2D array to store the values of c
    c = [[0] * m for _ in range(n)]
    
    # Populate the array c with the values of c_ij
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i] * b[j]
    
    # Initialize a variable to store the maximum area of the subrectangle
    max_area = 0
    
    # Iterate over all possible positions of the subrectangle
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    # Calculate the area of the current subrectangle
                    area = (k - i + 1) * (l - j + 1)
                    
                    # Calculate the sum of the elements in the current subrectangle
                    sum_elements = sum(sum(c[i:k+1], []))
                    
                    # Check if the sum of the elements is less than or equal to x
                    if sum_elements <= x:
                        # Update the maximum area if necessary
                        max_area = max(max_area, area)
    
    return max_area

def f2(n, m, a, b, x):
    # Initialize a 2D array to store the values of c
    c = [[0] * m for _ in range(n)]
    
    # Populate the array c with the values of c_ij
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i] * b[j]
    
    # Initialize a variable to store the maximum area of the subrectangle
    max_area = 0
    
    # Iterate over all possible positions of the subrectangle
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    # Calculate the area of the current subrectangle
                    area = (k - i + 1) * (l - j + 1)
                    
                    # Calculate the sum of the elements in the current subrectangle
                    sum_elements = sum(sum(c[i:k+1], []))
                    
                    # Check if the sum of the elements is less than or equal to x
                    if sum_elements <= x:
                        # Update the maximum area if necessary
                        max_area = max(max_area, area)
    
    return max_area

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = int(input())
    
    print(f1(n, m, a, b, x))
    print(f2(n, m, a, b, x))

