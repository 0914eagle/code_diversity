
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

def find_arrangement(a, b, c, R, C):
    if a + b + c != R * C:
        return "impossible"
    arrangement = []
    for i in range(R):
        row = []
        for j in range(C):
            if a > 0:
                row.append("A")
                a -= 1
            elif b > 0:
                row.append("B")
                b -= 1
            else:
                row.append("C")
                c -= 1
        arrangement.append(row)
    if is_valid_arrangement(arrangement, R, C):
        return arrangement
    else:
        return "impossible"

if __name__ == '__main__':
    R, C = map(int, input().split())
    a, b, c = map(int, input().split())
    print(find_arrangement(a, b, c, R, C))

