
def get_platforms(points, k):
    platforms = []
    for i in range(len(points)):
        x, y = points[i]
        platforms.append((x, x + k, y))
    return platforms

def get_saved_points(platforms, points):
    saved_points = []
    for i in range(len(points)):
        x, y = points[i]
        collides = False
        for platform in platforms:
            lx, rx, ly = platform
            if lx <= x <= rx and ly == y:
                collides = True
                break
        if not collides:
            saved_points.append((x, y))
    return saved_points

def get_max_saved_points(platforms, points):
    return len(get_saved_points(platforms, points))

def get_optimal_platforms(points, k):
    platforms = get_platforms(points, k)
    max_saved_points = 0
    optimal_platforms = []
    for i in range(len(platforms)):
        for j in range(i+1, len(platforms)):
            platforms1 = platforms[:i] + platforms[i:j] + platforms[j+1:]
            saved_points = get_saved_points(platforms1, points)
            if len(saved_points) > max_saved_points:
                max_saved_points = len(saved_points)
                optimal_platforms = platforms1
    return optimal_platforms

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        optimal_platforms = get_optimal_platforms(points, k)
        print(get_max_saved_points(optimal_platforms, points))

if __name__ == '__main__':
    main()

