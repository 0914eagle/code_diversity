
def count_nubs(height, width, mark):
    nubs = 0
    for i in range(height):
        for j in range(width):
            if mark[i][j] == '#':
                nubs += 1
    return nubs

def find_min_nubs(height, width, mark):
    nubs = count_nubs(height, width, mark)
    return nubs // 2

if __name__ == "__main__":
    height, width = map(int, input().split())
    mark = [input() for _ in range(height)]
    min_nubs = find_min_nubs(height, width, mark)
    print(min_nubs)
