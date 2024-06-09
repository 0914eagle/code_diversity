
def get_stamp_size(mark):
    stamp_size = 1
    for i in range(len(mark)):
        if mark[i] == '#':
            stamp_size += 1
    return stamp_size

def get_min_nubs(mark):
    stamp_size = get_stamp_size(mark)
    min_nubs = stamp_size
    for i in range(len(mark)):
        if mark[i] == '#':
            min_nubs = min(min_nubs, stamp_size - i)
    return min_nubs

def main():
    mark = [line.strip() for line in input().splitlines()]
    print(get_min_nubs(mark))

if __name__ == '__main__':
    main()

