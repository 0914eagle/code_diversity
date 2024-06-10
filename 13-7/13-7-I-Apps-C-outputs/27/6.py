
def get_good_arrangement(r, c, a, b, c):
    if a + b + c != r * c:
        return "impossible"
    
    tray = [[0] * c for _ in range(r)]
    for i in range(a):
        tray[i][i % c] = "A"
    for i in range(a, a + b):
        tray[i][(i - a) % c] = "B"
    for i in range(a + b, a + b + c):
        tray[i][(i - a - b) % c] = "C"
    
    for i in range(r):
        for j in range(c):
            if tray[i][j] != "A" and tray[i][(j - 1) % c] == tray[i][j]:
                return "impossible"
            if tray[i][j] != "B" and tray[i][(j - 1) % c] == tray[i][j]:
                return "impossible"
            if tray[i][j] != "C" and tray[i][(j - 1) % c] == tray[i][j]:
                return "impossible"
    
    return ["".join(row) for row in tray]

def main():
    r, c = map(int, input().split())
    a, b, c = map(int, input().split())
    print("\n".join(get_good_arrangement(r, c, a, b, c)))

if __name__ == '__main__':
    main()

