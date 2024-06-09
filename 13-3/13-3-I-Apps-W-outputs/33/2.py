
import math

def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the angle of the arrow vector
    angle = math.atan2(vy, vx)
    
    # Calculate the coordinates of the arrow points
    x1 = px + a * math.cos(angle)
    y1 = py + a * math.sin(angle)
    x2 = px + b * math.cos(angle + math.pi / 2)
    y2 = py + b * math.sin(angle + math.pi / 2)
    x3 = px + c * math.cos(angle + math.pi)
    y3 = py + c * math.sin(angle + math.pi)
    x4 = px + d * math.cos(angle + 3 * math.pi / 2)
    y4 = py + d * math.sin(angle + 3 * math.pi / 2)
    
    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

def main():
    px, py, vx, vy, a, b, c, d = map(float, input().split())
    points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    for x, y in points:
        print(x, y)

if __name__ == '__main__':
    main()

