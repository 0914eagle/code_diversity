
def f1(L, n, points):
    # Initialize a list to store the positions of the points
    pos = [0] * (L + 1)

    # Iterate through the points and mark their positions in the list
    for i in range(n):
        point, direction = points[i]
        if direction == "C":
            pos[point] = 1
        else:
            pos[point] = -1

    # Check if the wire touches itself at any point
    for i in range(1, L):
        if pos[i] == pos[i - 1]:
            return "GHOST"

    return "SAFE"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    L, n = map(int, input().split())
    points = []
    for i in range(n):
        point, direction = map(int, input().split())
        points.append((point, direction))

    print(f1(L, n, points))

