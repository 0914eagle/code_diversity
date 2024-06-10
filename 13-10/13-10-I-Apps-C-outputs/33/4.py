
def get_sets(points, l, r, a):
    sets = []
    for i in range(len(points)):
        x, y = points[i]
        if l < x < r and y > a:
            sets.append(i)
    return sets

def count_sets(sets):
    count = 0
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            if sets[i] != sets[j]:
                count += 1
    return count

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    l, r, a = map(int, input().split())
    sets = get_sets(points, l, r, a)
    count = count_sets(sets)
    print(count)

if __name__ == '__main__':
    main()

