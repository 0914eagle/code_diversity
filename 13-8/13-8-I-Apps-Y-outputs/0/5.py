
def get_input():
    return int(input())

def get_points(x):
    k = 0
    while x > 1:
        y = x
        while y % 2 == 0:
            y //= 2
            k += 1
        x = y
    return k

def main():
    x = get_input()
    print(get_points(x))

if __name__ == '__main__':
    main()

