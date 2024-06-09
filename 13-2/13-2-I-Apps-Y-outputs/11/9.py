
def check_sheep_and_wolves(sheep, wolves):
    if wolves >= sheep:
        return "unsafe"
    else:
        return "safe"

if __name__ == '__main__':
    sheep, wolves = map(int, input().split())
    print(check_sheep_and_wolves(sheep, wolves))

