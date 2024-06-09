
def is_valid_walk(walk, x_1, x_2, y_1, y_2):
    for i in range(len(walk) - 1):
        if not (x_1 <= walk[i][0] <= x_2 and y_1 <= walk[i][1] <= y_2):
            return False
    return True

def find_walk(a, b, c, d, x, y, x_1, x_2, y_1, y_2):
    walk = [(x, y)]
    while len(walk) < a + b + c + d:
        if len(walk) < a:
            walk.append((walk[-1][0] - 1, walk[-1][1]))
        elif len(walk) < a + b:
            walk.append((walk[-1][0] + 1, walk[-1][1]))
        elif len(walk) < a + b + c:
            walk.append((walk[-1][0], walk[-1][1] - 1))
        else:
            walk.append((walk[-1][0], walk[-1][1] + 1))
    return walk if is_valid_walk(walk, x_1, x_2, y_1, y_2) else None

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x_1, y_1, x_2, y_2 = map(int, input().split())
        walk = find_walk(a, b, c, d, x, y, x_1, x_2, y_1, y_2)
        if walk:
            print("YES")
            for node in walk:
                print(node[0], node[1])
        else:
            print("NO")

if __name__ == '__main__':
    main()

