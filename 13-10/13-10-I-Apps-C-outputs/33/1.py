
def get_points(n):
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def get_sets(points, l, r, a):
    sets = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            set_ = set()
            for k in range(len(points)):
                if l < points[i][0] < r and points[i][1] > a and points[j][0] < r and points[j][1] > a and points[k][0] < r and points[k][1] > a:
                    set_.add(points[k])
            if len(set_) > 0:
                sets.append(set_)
    return sets

def count_sets(sets):
    count = 0
    for set_ in sets:
        if len(set_) > 0:
            count += 1
    return count

def main():
    n = int(input())
    points = get_points(n)
    l, r, a = map(int, input().split())
    sets = get_sets(points, l, r, a)
    count = count_sets(sets)
    print(count)

if __name__ == '__main__':
    main()

