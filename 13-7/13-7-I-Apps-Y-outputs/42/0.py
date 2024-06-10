
def calculate(a, b):
    if a == 1:
        return b
    if a == 2:
        return b * 2
    if a == 3:
        return b * 3
    if a == 4:
        return b * 4
    if a == 5:
        return b * 5
    if a == 6:
        return b * 6
    if a == 7:
        return b * 7
    if a == 8:
        return b * 8
    if a == 9:
        return b * 9
    return -1

def main():
    a, b = map(int, input().split())
    result = calculate(a, b)
    print(result)

if __name__ == '__main__':
    main()

