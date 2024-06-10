
def is_good_arrangement(arrangement, R, C):
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == arrangement[i][j-1] and arrangement[i][j] != "0":
                return False
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == arrangement[i-1][j] and arrangement[i][j] != "0":
                return False
    return True

def find_good_arrangement(A, B, C, R, C):
    arrangement = [["0"] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A > 0:
                arrangement[i][j] = "A"
                A -= 1
            elif B > 0:
                arrangement[i][j] = "B"
                B -= 1
            else:
                arrangement[i][j] = "C"
                C -= 1
    if is_good_arrangement(arrangement, R, C):
        return arrangement
    else:
        return "impossible"

def main():
    R, C = map(int, input().split())
    A, B, C = map(int, input().split())
    arrangement = find_good_arrangement(A, B, C, R, C)
    if arrangement == "impossible":
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

