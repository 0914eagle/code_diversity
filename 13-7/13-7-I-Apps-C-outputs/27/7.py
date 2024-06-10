
def is_good_arrangement(arrangement, flavors):
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and arrangement[i][j] != "0":
                return False
    for i in range(len(arrangement[0])):
        for j in range(len(arrangement)):
            if arrangement[j][i] == arrangement[j-1][i] and arrangement[j][i] != "0":
                return False
    return True

def find_good_arrangement(flavors, rows, cols):
    arrangement = [["0"] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if flavors[0] > 0:
                arrangement[i][j] = "A"
                flavors[0] -= 1
            elif flavors[1] > 0:
                arrangement[i][j] = "B"
                flavors[1] -= 1
            else:
                arrangement[i][j] = "C"
                flavors[2] -= 1
    if is_good_arrangement(arrangement, flavors):
        return arrangement
    else:
        return "impossible"

def main():
    rows, cols = map(int, input().split())
    flavors = list(map(int, input().split()))
    arrangement = find_good_arrangement(flavors, rows, cols)
    if arrangement == "impossible":
        print("impossible")
    else:
        for i in range(len(arrangement)):
            print("".join(arrangement[i]))

if __name__ == '__main__':
    main()

