
def calculate(a, b):
    if a == 1:
        return b
    if b == 1:
        return a
    if a == 2:
        if b == 2 or b == 4 or b == 8:
            return 4
        return -1
    if a == 3:
        if b == 3:
            return 9
        return -1
    if a == 4:
        if b == 2 or b == 8:
            return 8
        return -1
    if a == 5:
        if b == 5:
            return 25
        return -1
    if a == 6:
        if b == 6:
            return 36
        return -1
    if a == 7:
        if b == 7:
            return 49
        return -1
    if a == 8:
        if b == 2 or b == 4 or b == 8:
            return 64
        return -1
    if a == 9:
        if b == 9:
            return 81
        return -1
    return -1

def main():
    a, b = map(int, input().split())
    result = calculate(a, b)
    if result != -1:
        print(result)
    else:
        print(-1)

if __name__ == '__main__':
    main()

