
def compare(x, a):
    if x < a:
        return 0
    else:
        return 10

if __name__ == '__main__':
    x, a = map(int, input().split())
    print(compare(x, a))

