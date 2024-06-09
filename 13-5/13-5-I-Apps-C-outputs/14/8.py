
def f1(L, n):
    # f1 function to read the input data
    points = []
    for i in range(n):
        point, direction = map(int, input().split())
        points.append((point, direction))
    return L, n, points

def f2(L, n, points):
    # f2 function to check if the wire will touch itself
    wire = [0] * (L + 1)
    for point, direction in points:
        if direction == 0:
            wire[point] = 1
        else:
            wire[point] = -1
        for i in range(point, L + 1):
            if wire[i] != 0 and wire[i - 1] != 0 and wire[i] + wire[i - 1] != 0:
                return "GHOST"
    return "SAFE"

if __name__ == '__main__':
    L, n, points = f1(int(input()), int(input()))
    print(f2(L, n, points))

