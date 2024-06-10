
def get_input():
    return list(map(int, input().split()))

def is_valid(x, y):
    if x < 1 or x > 100:
        return False
    if y < 1 or y > 100:
        return False
    if x * 2 + y % 4 != 0:
        return False
    return True

def main():
    x, y = get_input()
    if is_valid(x, y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

