
def get_shuffle_count(deck_size, shuffle_type):
    if shuffle_type == "out":
        return (deck_size // 2) + 1
    else:
        return deck_size

def main():
    while True:
        try:
            deck_size = int(input())
            shuffle_type = input()
            print(get_shuffle_count(deck_size, shuffle_type))
        except EOFError:
            break

if __name__ == '__main__':
    main()

