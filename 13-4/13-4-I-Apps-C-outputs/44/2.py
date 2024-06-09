
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid and find the maximum sub-rectangle with the given length-width ratio
    for i in range(x, n):
        for j in range(y, m):
            if i - x + 1 > a and j - y + 1 > b:
                x2, y2 = i, j
            if i - x + 1 == a and j - y + 1 == b:
                x2, y2 = i, j
                break
        if x2 == n:
            break
    
    return x1, y1, x2, y2

def find_closest_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid and find the sub-rectangle that is closest to (x, y)
    for i in range(x, n):
        for j in range(y, m):
            if (i - x) ** 2 + (j - y) ** 2 < (x2 - x1) ** 2 + (y2 - y1) ** 2:
                x1, y1, x2, y2 = i, j, i, j
            if (i - x) ** 2 + (j - y) ** 2 == (x2 - x1) ** 2 + (y2 - y1) ** 2:
                x1, y1, x2, y2 = i, j, i, j
                break
        if x2 == n:
            break
    
    return x1, y1, x2, y2

def find_lexicographically_min_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid and find the sub-rectangle that is lexicographically minimum
    for i in range(x, n):
        for j in range(y, m):
            if (i, j, x2, y2) < (x1, y1, x2, y2):
                x1, y1, x2, y2 = i, j, x2, y2
            if (i, j, x2, y2) == (x1, y1, x2, y2):
                x1, y1, x2, y2 = i, j, x2, y2
                break
        if x2 == n:
            break
    
    return x1, y1, x2, y2

if __name__ == '__main__':
    n, m, x, y, a, b = map(int, input().split())
    print(*find_sub_rectangle(n, m, x, y, a, b))
    print(*find_closest_sub_rectangle(n, m, x, y, a, b))
    print(*find_lexicographically_min_sub_rectangle(n, m, x, y, a, b))

