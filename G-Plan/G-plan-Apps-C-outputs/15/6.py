
def count_nubs(n, m, mark):
    nubs = 0
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                nubs += 1
    return nubs

def solve_stamp_problem():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    
    nubs = count_nubs(n, m, mark)
    print(nubs)

if __name__ == "__main__":
    solve_stamp_problem()
