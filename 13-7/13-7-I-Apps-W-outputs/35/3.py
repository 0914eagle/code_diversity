
def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the angle of the arrow vector
    angle = np.arctan2(vy, vx)
    
    # Calculate the coordinates of the arrow points
    points = []
    for i in range(3):
        x = px + a * np.cos(angle + i * np.pi / 2)
        y = py + b * np.sin(angle + i * np.pi / 2)
        points.append((x, y))
    
    return points

def main():
    # Read the input
    px, py, vx, vy, a, b, c, d = map(int, input().split())
    
    # Calculate the arrow points
    points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    
    # Print the output
    for point in points:
        print(point[0], point[1])

if __name__ == '__main__':
    main()

