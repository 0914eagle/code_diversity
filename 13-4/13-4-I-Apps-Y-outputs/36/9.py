
def read_input():
    return map(int, input().split())

def compare(x, a):
    if x < a:
        return 0
    else:
        return 10

def main():
    x, a = read_input()
    print(compare(x, a))

if __name__ == '__main__':
    main()

