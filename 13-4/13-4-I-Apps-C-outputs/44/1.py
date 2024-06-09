
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid and expand the sub-rectangle in all four directions
    for i in range(x1, n+1):
        for j in range(y1, m+1):
            if i == x1 and j == y1:
                continue
            if (i-x1)/(j-y1) == a/b:
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)
    
    return x1, y1, x2, y2

def main():
    n, m, x, y, a, b = map(int, input().split())
    x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
    print(x1, y1, x2, y2)

if __name__ == '__main__':
    main()

