
def count_nubs(height, width, mark):
    nubs = 0
    for i in range(height):
        for j in range(width):
            if mark[i][j] == '#':
                nubs += 1
    return nubs

def solve_stamp_problem():
    height, width = map(int, input().split())
    mark = [input() for _ in range(height)]
    
    nubs = count_nubs(height, width, mark)
    print(nubs)

if __name__ == "__main__":
    solve_stamp_problem()
