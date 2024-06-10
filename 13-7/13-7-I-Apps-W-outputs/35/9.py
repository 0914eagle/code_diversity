
import math

def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the angle of the arrow direction vector
    angle = math.atan2(vy, vx)
    
    # Calculate the coordinates of the arrow points
    points = []
    points.append((px + a * math.cos(angle), py + a * math.sin(angle)))
    points.append((px + a * math.cos(angle + math.pi / 2), py + a * math.sin(angle + math.pi / 2)))
    points.append((px + c * math.cos(angle + math.pi), py + c * math.sin(angle + math.pi)))
    points.append((px + c * math.cos(angle + math.pi / 2), py + c * math.sin(angle + math.pi / 2)))
    points.append((px + d * math.cos(angle + math.pi / 2), py + d * math.sin(angle + math.pi / 2)))
    points.append((px + d * math.cos(angle), py + d * math.sin(angle)))
    points.append((px + c * math.cos(angle), py + c * math.sin(angle)))
    
    return points

def main():
    px, py, vx, vy, a, b, c, d = map(int, input().split())
    points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    for point in points:
        print(f"{point[0]:.9f} {point[1]:.9f}")

if __name__ == '__main__':
    main()

