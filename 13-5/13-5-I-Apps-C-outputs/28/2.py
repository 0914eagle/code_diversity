
def f1(n, m, y1, y2):
    # find the maximum number of enemy spaceships that can be destroyed
    max_dest = 0
    for i in range(len(y1)):
        for j in range(len(y2)):
            if y1[i] == y2[j]:
                max_dest += 1
    return max_dest

def f2(n, m, y1, y2):
    # find the positions where the small spaceships can be positioned to destroy the maximum number of enemy spaceships
    positions = []
    for i in range(len(y1)):
        for j in range(len(y2)):
            if y1[i] == y2[j]:
                positions.append((0, y1[i]))
    return positions

if __name__ == '__main__':
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    print(f1(n, m, y1, y2))
    print(f2(n, m, y1, y2))

