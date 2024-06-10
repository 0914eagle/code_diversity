
def get_result(x, y, z):
    if x + y == 0:
        return "?"
    if x > y:
        return "+"
    if x < y:
        return "-"
    return "0"

def main():
    x, y, z = map(int, input().split())
    print(get_result(x, y, z))

if __name__ == '__main__':
    main()

