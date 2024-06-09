
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the points inside the sub-rectangle
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            # If the point is outside the rectangle, update the sub-rectangle
            if i < x1 or i > x2 or j < y1 or j > y2:
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)
    
    # Check if the length-width ratio is correct
    if x2-x1 != a*y2-y1:
        return None
    
    return x1, y1, x2, y2

def main():
    n, m, x, y, a, b = map(int, input().split())
    sub_rectangle = find_sub_rectangle(n, m, x, y, a, b)
    if sub_rectangle is None:
        print("No sub-rectangle found")
    else:
        print(*sub_rectangle)

if __name__ == '__main__':
    main()

