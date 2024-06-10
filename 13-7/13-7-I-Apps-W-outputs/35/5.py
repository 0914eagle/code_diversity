
def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the coordinates of the arrow points
    x1 = px + vx
    y1 = py + vy
    x2 = px + vx - a
    y2 = py + vy - b
    x3 = px + vx - c
    y3 = py + vy - d
    x4 = px + vx - c + a
    y4 = py + vy - d + b
    x5 = px + vx - c + a - b
    y5 = py + vy - d + b - a
    
    # Return the coordinates of the arrow points in counter-clockwise order
    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]

def main():
    # Read the input
    px, py, vx, vy, a, b, c, d = map(int, input().split())
    
    # Calculate the arrow points
    arrow_points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    
    # Print the arrow points
    for point in arrow_points:
        print(point[0], point[1])

if __name__ == '__main__':
    main()

