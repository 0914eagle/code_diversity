
def find_sets(points, left, bottom, right):
    sets = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i][0] < right and points[i][0] > left and points[i][1] > bottom and points[j][0] < right and points[j][0] > left and points[j][1] > bottom:
                set_ = [points[i], points[j]]
                sets.append(set_)
    return sets

def count_unique_sets(sets):
    unique_sets = []
    for set_ in sets:
        if set_ not in unique_sets:
            unique_sets.append(set_)
    return len(unique_sets)

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    left, bottom, right = map(int, input().split())
    sets = find_sets(points, left, bottom, right)
    print(count_unique_sets(sets))

if __name__ == '__main__':
    main()

