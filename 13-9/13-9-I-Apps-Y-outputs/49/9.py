
def shuffle(deck_size, shuffle_type):
    if shuffle_type == "out":
        return deck_size // 2
    else:
        return deck_size - 1

def main():
    while True:
        try:
            deck_size = int(input())
            shuffle_type = input()
            print(shuffle(deck_size, shuffle_type))
        except EOFError:
            break

if __name__ == '__main__':
    main()

