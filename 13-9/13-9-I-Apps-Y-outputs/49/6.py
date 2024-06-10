
def get_shuffle_count(n, shuffle_type):
    if shuffle_type == "out":
        return n // 2
    elif shuffle_type == "in":
        return n // 2 + 1
    else:
        raise ValueError("Invalid shuffle type")

def main():
    while True:
        try:
            n = int(input())
            shuffle_type = input()
            print(get_shuffle_count(n, shuffle_type))
        except EOFError:
            break

if __name__ == '__main__':
    main()

