
def read_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def get_line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, C

def check_intersection(p1, p2, q1, q2):
    A1, B1, C1 = get_line(p1, p2)
    A2, B2, C2 = get_line(q1, q2)
    D = A1 * B2 - A2 * B1
    if D == 0:
        return False
    x = (B2 * C1 - B1 * C2) / D
    y = (A1 * C2 - A2 * C1) / D
    return x >= min(p1[0], p2[0]) and x <= max(p1[0], p2[0]) and y >= min(p1[1], p2[1]) and y <= max(p1[1], p2[1])

def perfect_matching(R, B, rebels, bases):
    visited = [False] * R
    matching = [-1] * B
    for i in range(R):
        for j in range(B):
            if not visited[i] and matching[j] == -1 and not check_intersection(rebels[i], bases[j], rebels[i], bases[(j+1)%B]):
                visited[i] = True
                matching[j] = i
                break
    for i in range(R):
        if not visited[i]:
            return False
    return True

def main():
    R, B, rebels, bases = read_input()
    print("Yes") if perfect_matching(R, B, rebels, bases) else print("No")

if __name__ == '__main__':
    main()

