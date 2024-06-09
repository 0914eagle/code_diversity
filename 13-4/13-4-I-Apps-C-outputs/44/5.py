
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid points in the x-direction
    for i in range(x+1, n+1):
        # If the current point is within the sub-rectangle, update the sub-rectangle
        if i <= x2 and (i-x1)*b == (y2-y1)*a:
            x2 = i
        # If the current point is outside the sub-rectangle, break the loop
        else:
            break
    
    # Iterate through the grid points in the y-direction
    for j in range(y+1, m+1):
        # If the current point is within the sub-rectangle, update the sub-rectangle
        if j <= y2 and (j-y1)*a == (x2-x1)*b:
            y2 = j
        # If the current point is outside the sub-rectangle, break the loop
        else:
            break
    
    return x1, y1, x2, y2

def main():
    n, m, x, y, a, b = map(int, input().split())
    x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
    print(x1, y1, x2, y2)

if __name__ == '__main__':
    main()

