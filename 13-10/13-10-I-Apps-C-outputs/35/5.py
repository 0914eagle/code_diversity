
def get_cards(x, y):
    if x == 0 and y == 0:
        return "Impossible"
    if x == 0 or y == 0:
        return "1B" * max(x, y)
    if x == 1 and y == 1:
        return "AB"
    if x == 1 or y == 1:
        return "1A1B"
    if x == 2 and y == 2:
        return "1A1B"
    if x == 3 and y == 2:
        return "1A1B1A1B"
    if x == 4 and y == 2:
        return "1A1B1A1B1A1B"
    if x == 5 and y == 2:
        return "1A1B1A1B1A1B1A1B"
    if x == 6 and y == 2:
        return "1A1B1A1B1A1B1A1B1A1B"
    if x == 7 and y == 2:
        return "1A1B1A1B1A1B1A1B1A1B1A1B"
    if x == 8 and y == 2:
        return "1A1B1A1B1A1B1A1B1A1B1A1B1A1B"
    if x == 9 and y == 2:
        return "1A1B1A1B1A1B1A1B1A1B1A1B1A1B1A1B"
    if x == 10 and y == 2:
        return "1A1B1A1B1A1B1A1B1A1B1A1B1A1B1A1B1A1B"
    return "Impossible"

def main():
    x, y = map(int, input().split())
    print(get_cards(x, y))

if __name__ == '__main__':
    main()

