
def get_cards(x, y):
    if x == 0 and y == 0:
        return "Impossible"
    if x == 0:
        return "A" * y
    if y == 0:
        return "B" * x
    return "A" * x + "B" * y

def main():
    x, y = map(int, input().split())
    print(get_cards(x, y))

if __name__ == '__main__':
    main()

