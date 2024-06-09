
def is_unsafe(sheep, wolves):
    if wolves >= sheep:
        return "unsafe"
    else:
        return "safe"

if __name__ == '__main__':
    sheep, wolves = map(int, input().split())
    print(is_unsafe(sheep, wolves))

