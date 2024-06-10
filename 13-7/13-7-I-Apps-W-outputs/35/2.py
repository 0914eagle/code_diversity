
def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the angle of the arrow
    angle = math.atan2(vy, vx)
    
    # Calculate the coordinates of the arrow points
    points = []
    for i in range(3):
        x = px + a * math.cos(angle + i * math.pi / 2)
        y = py + a * math.sin(angle + i * math.pi / 2)
        points.append((x, y))
    
    return points

def main():
    # Read the input
    px, py, vx, vy, a, b, c, d = map(int, input().split())
    
    # Calculate the arrow points
    points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    
    # Print the output
    for x, y in points:
        print(x, y)

if __name__ == '__main__':
    main()

