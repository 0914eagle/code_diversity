
def is_valid_arrangement(arrangement, R, C):
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == arrangement[i][j-1] and j > 0:
                return False
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == arrangement[i-1][j] and i > 0:
                return False
    return True

def get_arrangement(a, b, c, R, C):
    if a + b + c != R * C:
        return "impossible"
    arrangement = [[0] * C for _ in range(R)]
    i, j = 0, 0
    while i < R and j < C:
        if arrangement[i][j] == 0:
            arrangement[i][j] = "A"
            a -= 1
        elif arrangement[i][j] == 1:
            arrangement[i][j] = "B"
            b -= 1
        else:
            arrangement[i][j] = "C"
            c -= 1
        j += 1
        if j == C:
            i += 1
            j = 0
    if a != 0 or b != 0 or c != 0:
        return "impossible"
    return arrangement

def main():
    R, C = map(int, input().split())
    a, b, c = map(int, input().split())
    arrangement = get_arrangement(a, b, c, R, C)
    if arrangement == "impossible":
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

