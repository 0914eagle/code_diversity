
def find_rectangle(n, m, x, y, a, b):
    # Initialize the rectangle coordinates
    x1, y1, x2, y2 = 0, 0, n, m
    
    # Loop through all possible rectangle sizes
    for i in range(n):
        for j in range(m):
            # Check if the current rectangle size is valid
            if x1 + i <= x and y1 + j <= y and x2 - i >= x and y2 - j >= y:
                # Check if the current rectangle has the correct length-width ratio
                if (x2 - x1) / (y2 - y1) == a / b:
                    return x1 + i, y1 + j, x2 - i, y2 - j
    
    # If no rectangle is found, return None
    return None

def main():
    n, m, x, y, a, b = map(int, input().split())
    rectangle = find_rectangle(n, m, x, y, a, b)
    if rectangle is None:
        print("No rectangle found")
    else:
        print(*rectangle)

if __name__ == '__main__':
    main()

