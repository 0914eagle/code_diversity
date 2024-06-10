
def get_input():
    n = int(input())
    corners = []
    for i in range(n):
        r, c = map(int, input().split())
        corners.append((r, c))
    return n, corners

def get_matching(n, corners):
    matching = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if is_matching(corners[i], corners[j]):
                matching[i] = j
                matching[j] = i
                break
    
    if any(matching[i] == 0 for i in range(n)):
        return "syntax error"
    else:
        return "".join(str(matching[i]) for i in range(n))

def is_matching(corner1, corner2):
    r1, c1 = corner1
    r2, c2 = corner2
    return r1 <= r2 and c1 <= c2 and (r1 == r2 or c1 == c2)

def main():
    n, corners = get_input()
    print(get_matching(n, corners))

if __name__ == '__main__':
    main()

