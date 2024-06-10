
def get_shuffle_count(n, shuffle_type):
    if shuffle_type == "out":
        return n // 2
    else:
        return n - 1

def main():
    n = int(input())
    shuffle_type = input()
    print(get_shuffle_count(n, shuffle_type))

if __name__ == '__main__':
    main()

