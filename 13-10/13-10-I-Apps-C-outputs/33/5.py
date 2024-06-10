
def get_area_points(points, area):
    left, bottom, right = area
    return [point for point in points if left < point[0] < right and point[1] > bottom]

def count_non_empty_sets(points, area):
    area_points = get_area_points(points, area)
    return len(set(map(tuple, area_points)))

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    area = tuple(map(int, input().split()))
    print(count_non_empty_sets(points, area))

if __name__ == '__main__':
    main()

