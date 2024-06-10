
def get_result(x, y, z):
    total_votes = x + y
    if total_votes == 0:
        return "?"
    if x > y:
        return "+"
    elif x < y:
        return "-"
    else:
        return "0"

def main():
    x, y, z = map(int, input().split())
    print(get_result(x, y, z))

if __name__ == '__main__':
    main()

