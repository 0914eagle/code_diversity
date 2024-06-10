
def get_points(n):
    points = []
    for i in range(n):
        x = int(input())
        points.append(x)
    return points

def get_subset(points):
    subset = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i] - points[j] == 2**d for d in range(32):
                subset.append(points[i])
                subset.append(points[j])
                break
    return subset

def main():
    n = int(input())
    points = get_points(n)
    subset = get_subset(points)
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    main()

