
def f1(n, m, a, b, x):
    # Initialize a 2D array to store the values of c
    c = [[0] * (m+1) for _ in range(n+1)]
    
    # Build the array c
    for i in range(1, n+1):
        for j in range(1, m+1):
            c[i][j] = a[i-1] * b[j-1]
    
    # Initialize the maximum area and the corresponding subrectangle
    max_area = 0
    subrectangle = []
    
    # Iterate over all possible subrectangles
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i, n+1):
                for l in range(j, m+1):
                    # Calculate the area of the current subrectangle
                    area = (k-i+1) * (l-j+1)
                    
                    # Check if the area is valid and if the sum of the elements is less than or equal to x
                    if area > max_area and sum(sum(c[i:k+1], [])) <= x:
                        max_area = area
                        subrectangle = [i, k, j, l]
    
    # Return the maximum area
    return max_area

def f2(n, m, a, b, x):
    # Initialize a 2D array to store the values of c
    c = [[0] * (m+1) for _ in range(n+1)]
    
    # Build the array c
    for i in range(1, n+1):
        for j in range(1, m+1):
            c[i][j] = a[i-1] * b[j-1]
    
    # Initialize the maximum area and the corresponding subrectangle
    max_area = 0
    subrectangle = []
    
    # Iterate over all possible subrectangles
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i, n+1):
                for l in range(j, m+1):
                    # Calculate the area of the current subrectangle
                    area = (k-i+1) * (l-j+1)
                    
                    # Check if the area is valid and if the sum of the elements is less than or equal to x
                    if area > max_area and sum(sum(c[i:k+1], [])) <= x:
                        max_area = area
                        subrectangle = [i, k, j, l]
    
    # Return the maximum area
    return max_area

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = int(input())
    
    print(f1(n, m, a, b, x))
    print(f2(n, m, a, b, x))

