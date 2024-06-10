
def shuffle(n, type):
    if type == "out":
        return (n // 2) * 2
    elif type == "in":
        return (n // 2) * 2 + 1

def main():
    n, type = map(int, input().split())
    print(shuffle(n, type))

if __name__ == '__main__':
    main()

