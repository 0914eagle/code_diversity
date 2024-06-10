
def check_arrangement(arrangement):
    # Check if the arrangement is a good arrangement
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and arrangement[i][j] != " ":
                return False
    return True

def find_arrangement(R, C, a, b, c):
    # Initialize the arrangement with all bonbons of flavor A
    arrangement = [["A"] * C for _ in range(R)]
    a_left = a
    b_left = b
    c_left = c
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == "A" and a_left > 0:
                arrangement[i][j] = "A"
                a_left -= 1
            elif arrangement[i][j] == "B" and b_left > 0:
                arrangement[i][j] = "B"
                b_left -= 1
            elif arrangement[i][j] == "C" and c_left > 0:
                arrangement[i][j] = "C"
                c_left -= 1
            if a_left == 0 and b_left == 0 and c_left == 0:
                break
        if a_left == 0 and b_left == 0 and c_left == 0:
            break
    if check_arrangement(arrangement):
        return arrangement
    else:
        return None

def main():
    R, C = map(int, input().split())
    a, b, c = map(int, input().split())
    arrangement = find_arrangement(R, C, a, b, c)
    if arrangement is None:
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

