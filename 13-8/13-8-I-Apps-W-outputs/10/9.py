
def compare(x, y):
    if x**y < y**x:
        return '<'
    elif x**y > y**x:
        return '>'
    else:
        return '='

def main():
    x, y = map(int, input().split())
    print(compare(x, y))

if __name__ == '__main__':
    main()

