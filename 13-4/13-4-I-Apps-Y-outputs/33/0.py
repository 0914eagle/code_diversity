
def f1(N, X, Y, A):
    # Calculate the area of the original polygon
    area = 0
    for i in range(N):
        area += X[i] * Y[i % N]
    
    # Calculate the ratio of the new area to the original area
    ratio = A / area
    
    # Calculate the new coordinates of the polygon points
    new_X = [int(X[i] * ratio) for i in range(N)]
    new_Y = [int(Y[i] * ratio) for i in range(N)]
    
    # Return the new coordinates
    return new_X, new_Y

def f2(N, X, Y, A):
    # Calculate the center of the original polygon
    center_x = sum(X) / N
    center_y = sum(Y) / N
    
    # Calculate the radius of the original polygon
    radius = ((sum((X - center_x) ** 2) + sum((Y - center_y) ** 2)) / N) ** 0.5
    
    # Calculate the angle of each point from the center
    angles = [atan2(Y[i] - center_y, X[i] - center_x) for i in range(N)]
    
    # Calculate the new radius of the polygon
    new_radius = A ** 0.5
    
    # Calculate the new coordinates of the polygon points
    new_X = [int(center_x + new_radius * cos(angles[i])) for i in range(N)]
    new_Y = [int(center_y + new_radius * sin(angles[i])) for i in range(N)]
    
    # Return the new coordinates
    return new_X, new_Y

if __name__ == '__main__':
    N = int(input())
    X = [float(x) for x in input().split()]
    Y = [float(y) for y in input().split()]
    A = int(input())
    
    new_X, new_Y = f1(N, X, Y, A)
    print(*new_X, sep='\n')
    print(*new_Y, sep='\n')

