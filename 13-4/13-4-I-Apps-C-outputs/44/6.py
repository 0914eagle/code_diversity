
def find_rectangle(n, m, x, y, a, b):
    # Initialize the rectangle coordinates
    x1, y1, x2, y2 = 0, 0, n, m
    
    # Loop through all possible rectangle coordinates
    for i in range(n):
        for j in range(m):
            # Check if the current coordinate is inside the rectangle
            if i <= x <= i + a and j <= y <= j + b:
                # Update the rectangle coordinates
                x1, y1, x2, y2 = i, j, i + a, j + b
    
    return x1, y1, x2, y2

def main():
    n, m, x, y, a, b = map(int, input().split())
    x1, y1, x2, y2 = find_rectangle(n, m, x, y, a, b)
    print(x1, y1, x2, y2)

if __name__ == '__main__':
    main()

