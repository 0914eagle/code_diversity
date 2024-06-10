
def is_good_arrangement(arrangement, a, b, c):
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and arrangement[i][j] != ' ':
                return False
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i-1][j] and arrangement[i][j] != ' ':
                return False
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] != ' ':
                if arrangement[i][j] == 'A':
                    a -= 1
                elif arrangement[i][j] == 'B':
                    b -= 1
                else:
                    c -= 1
    if a != 0 or b != 0 or c != 0:
        return False
    return True

def generate_arrangement(r, c, a, b, c):
    arrangement = [[' ' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a > 0:
                arrangement[i][j] = 'A'
                a -= 1
            elif b > 0:
                arrangement[i][j] = 'B'
                b -= 1
            else:
                arrangement[i][j] = 'C'
                c -= 1
    return arrangement

def main():
    r, c = map(int, input().split())
    a, b, c = map(int, input().split())
    arrangement = generate_arrangement(r, c, a, b, c)
    if is_good_arrangement(arrangement, a, b, c):
        for i in range(r):
            print("".join(arrangement[i]))
    else:
        print("impossible")

if __name__ == '__main__':
    main()

