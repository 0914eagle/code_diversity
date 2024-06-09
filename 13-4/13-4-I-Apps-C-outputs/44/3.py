
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid and find the maximum sub-rectangle with the given length-width ratio
    for i in range(x+1, n+1):
        for j in range(y+1, m+1):
            if i-x1 == a*(j-y1)//b:
                x2, y2 = i, j
    
    return x1, y1, x2, y2

def main():
    n, m, x, y, a, b = map(int, input().split())
    x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
    print(x1, y1, x2, y2)

if __name__ == '__main__':
    main()

