
def get_shuffles(deck_size, shuffle_type):
    if shuffle_type == "out":
        return (deck_size + 1) // 2
    else:
        return deck_size // 2

def main():
    while True:
        try:
            deck_size, shuffle_type = input().split()
            deck_size = int(deck_size)
            shuffle_type = shuffle_type.lower()
            if deck_size > 0 and shuffle_type in ["out", "in"]:
                print(get_shuffles(deck_size, shuffle_type))
            else:
                print("Invalid input")
        except EOFError:
            break

if __name__ == '__main__':
    main()

