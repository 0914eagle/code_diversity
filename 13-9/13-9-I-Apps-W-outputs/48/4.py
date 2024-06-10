
def get_result(x, y, z):
    if x + y + z == 0:
        return "?"
    if x + y + z == 1:
        return "+" if x > 0 else "-" if y > 0 else "0"
    if x + y + z == 2:
        return "+" if x > 0 and y == 0 else "-" if x == 0 and y > 0 else "0" if x == 0 and y == 0 else "?"
    if x + y + z == 3:
        return "+" if x > 0 and y == 0 and z == 0 else "-" if x == 0 and y > 0 and z == 0 else "0" if x == 0 and y == 0 and z > 0 else "?"
    return "?"

def main():
    x, y, z = map(int, input().split())
    print(get_result(x, y, z))

if __name__ == '__main__':
    main()

