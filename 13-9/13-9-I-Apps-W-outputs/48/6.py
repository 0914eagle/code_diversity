
def get_result(x, y, z):
    if x > y:
        return "+"
    elif x < y:
        return "-"
    else:
        return "0"

def is_result_uncertain(x, y, z):
    if x + y + z == 0:
        return False
    if x == 0 and y == 0 and z == 1:
        return True
    if x == 0 and y == 1 and z == 0:
        return True
    if x == 1 and y == 0 and z == 0:
        return True
    if x == 1 and y == 1 and z == 1:
        return True
    return False

def main():
    x, y, z = map(int, input().split())
    result = get_result(x, y, z)
    if is_result_uncertain(x, y, z):
        print("?")
    else:
        print(result)

if __name__ == '__main__':
    main()

