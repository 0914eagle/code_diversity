
def is_valid_arrangement(arrangement, a, b, c):
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and j > 0:
                return False
            if arrangement[i][j] == arrangement[i-1][j] and i > 0:
                return False
    return True

def find_good_arrangement(a, b, c):
    rows = a // c
    cols = b // a
    arrangement = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append("A")
        arrangement.append(temp)
    return arrangement

def main():
    r, c = map(int, input().split())
    a, b, c = map(int, input().split())
    if a + b + c != r * c:
        print("impossible")
        return
    arrangement = find_good_arrangement(a, b, c)
    if arrangement == []:
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

