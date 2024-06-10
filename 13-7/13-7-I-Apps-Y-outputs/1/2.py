
def get_input():
    return list(map(int, input().split()))

def is_valid_combination(x, y):
    for i in range(1, x+1):
        if i % 2 == 0:
            j = x - i
        else:
            j = x - i + 1
        if i + j == x and i * 2 + j * 4 == y:
            return True
    return False

def main():
    x, y = get_input()
    if is_valid_combination(x, y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

