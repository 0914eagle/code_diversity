
def is_good_arrangement(arrangement, a, b, c):
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and arrangement[i][j] != " ":
                return False
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i-1][j] and arrangement[i][j] != " ":
                return False
    return True

def find_good_arrangement(a, b, c):
    arrangement = [[" " for _ in range(c)] for _ in range(a)]
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        for i in range(a):
            for j in range(c):
                if i % 2 == 0 and j % 2 == 0:
                    arrangement[i][j] = "A"
                    a -= 1
                elif i % 2 == 1 and j % 2 == 1:
                    arrangement[i][j] = "B"
                    b -= 1
                else:
                    arrangement[i][j] = "C"
                    c -= 1
        if a == 0 and b == 0 and c == 0:
            return arrangement
        else:
            return "impossible"
    else:
        return "impossible"

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    r, c = map(int, input().split())
    arrangement = find_good_arrangement(a, b, c)
    if arrangement == "impossible":
        print("impossible")
    else:
        for i in range(r):
            print("".join(arrangement[i]))

