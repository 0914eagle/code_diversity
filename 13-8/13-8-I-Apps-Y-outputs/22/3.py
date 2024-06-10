
def get_input():
    n = int(input())
    a = [int(i) for i in input().split()]
    return n, a


def play_game(n, a):
    sheet = set()
    for i in range(n):
        if a[i] in sheet:
            sheet.remove(a[i])
        else:
            sheet.add(a[i])
    return len(sheet)


def main():
    n, a = get_input()
    print(play_game(n, a))


if __name__ == '__main__':
    main()

