
def get_stamp_size(mark):
    stamp_size = 1
    for i in range(1, len(mark)):
        if mark[i] != mark[i-1]:
            stamp_size += 1
    return stamp_size

def get_min_nubs(mark):
    stamp_size = get_stamp_size(mark)
    return stamp_size * stamp_size

def main():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    print(get_min_nubs(mark))

if __name__ == '__main__':
    main()

