
def get_stamp_size(mark):
    stamp_size = 1
    for i in range(len(mark)):
        if mark[i] == '#':
            stamp_size += 1
    return stamp_size

def get_min_nubs(mark):
    stamp_size = get_stamp_size(mark)
    return stamp_size * 2 - 1

def main():
    while True:
        try:
            n, m = map(int, input().split())
            mark = [input() for _ in range(n)]
            print(get_min_nubs(mark))
        except EOFError:
            break

if __name__ == '__main__':
    main()

