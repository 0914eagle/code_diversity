
def is_unsafe(sheep, wolves):
    if wolves >= sheep:
        return "unsafe"
    else:
        return "safe"

def main():
    sheep, wolves = map(int, input().split())
    print(is_unsafe(sheep, wolves))

if __name__ == '__main__':
    main()

