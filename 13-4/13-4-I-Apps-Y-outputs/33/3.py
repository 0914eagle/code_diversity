
def f1(N, points, A):
    # Calculate the area of the original polygon
    area = f2(N, points)
    
    # Calculate the ratio of the new area to the original area
    ratio = A / area
    
    # Calculate the new coordinates of the polygon points
    new_points = [(x * ratio, y * ratio) for x, y in points]
    
    # Return the new coordinates
    return new_points

def f2(N, points):
    # Calculate the area of the polygon
    area = 0
    for i in range(N):
        j = (i + 1) % N
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    area = abs(area) / 2
    
    # Return the area
    return area

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(float, input().split())
        points.append((x, y))
    A = int(input())
    new_points = f1(N, points, A)
    for x, y in new_points:
        print(f"{x:.4f} {y:.4f}")

