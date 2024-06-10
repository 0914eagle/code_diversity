
def read_input():
    N, M = map(int, input().split())
    return N, M

def solve(N, M):
    # Your code here
    pass

def write_output(solution):
    if solution is None:
        print(-1)
    else:
        for i in range(N*M):
            print(solution[i][0], solution[i][1])

if __name__ == '__main__':
    N, M = read_input()
    solution = solve(N, M)
    write_output(solution)

