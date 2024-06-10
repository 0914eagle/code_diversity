
import math

def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the angle of the arrow vector
    angle = math.atan2(vy, vx)
    
    # Calculate the coordinates of the arrow points
    x1 = px + a * math.cos(angle)
    y1 = py + a * math.sin(angle)
    x2 = x1 + b * math.cos(angle + math.pi / 2)
    y2 = y1 + b * math.sin(angle + math.pi / 2)
    x3 = x2 + c * math.cos(angle)
    y3 = y2 + c * math.sin(angle)
    x4 = x3 + d * math.cos(angle + math.pi / 2)
    y4 = y3 + d * math.sin(angle + math.pi / 2)
    
    # Return the arrow points in counter-clockwise order
    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

def main():
    # Read the input
    px, py, vx, vy, a, b, c, d = map(int, input().split())
    
    # Calculate the arrow points
    points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    
    # Print the arrow points
    for point in points:
        print(point[0], point[1])

if __name__ == '__main__':
    main()

