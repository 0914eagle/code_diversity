
def get_input():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    return n, m, mark

def get_stamp_size(mark):
    stamp_size = 1
    for row in mark:
        for col in row:
            if col == '#':
                stamp_size += 1
    return stamp_size

def get_stamp_pattern(mark):
    stamp_pattern = []
    for row in mark:
        for col in row:
            if col == '#':
                stamp_pattern.append(col)
    return stamp_pattern

def get_possible_stamps(n, m, mark):
    possible_stamps = []
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                possible_stamps.append(mark[i][j:j+1])
    return possible_stamps

def get_min_nubs(n, m, mark):
    stamp_size = get_stamp_size(mark)
    stamp_pattern = get_stamp_pattern(mark)
    possible_stamps = get_possible_stamps(n, m, mark)
    min_nubs = float('inf')
    for stamp in possible_stamps:
        stamp_nubs = stamp_pattern.count(stamp[0])
        if stamp_nubs < min_nubs:
            min_nubs = stamp_nubs
    return min_nubs

def main():
    n, m, mark = get_input()
    min_nubs = get_min_nubs(n, m, mark)
    print(min_nubs)

if __name__ == '__main__':
    main()

