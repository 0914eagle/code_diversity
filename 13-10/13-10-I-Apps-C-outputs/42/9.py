
def is_valid_arrangement(arrangement, a, b, c):
    for i in range(len(arrangement)):
        for j in range(i+1, len(arrangement)):
            if arrangement[i] == arrangement[j] and (i+1) % 2 == 0 and (j+1) % 2 == 0:
                return False
    return True

def find_good_arrangement(a, b, c):
    arrangement = []
    for i in range(a):
        arrangement.append("A")
    for i in range(b):
        arrangement.append("B")
    for i in range(c):
        arrangement.append("C")

    if is_valid_arrangement(arrangement, a, b, c):
        return arrangement
    else:
        return "impossible"

def main():
    r, c = map(int, input().split())
    a, b, c = map(int, input().split())
    print(find_good_arrangement(a, b, c))

if __name__ == '__main__':
    main()

