
def is_valid_solution(solution, n, k):
    for i in range(n):
        for j in range(n):
            if solution[i][j] != 0 and solution[i][j] != i + 1:
                return False
    for i in range(n):
        for j in range(n):
            if solution[i][j] != 0 and solution[j][i] != 0 and solution[i][j] != solution[j][i]:
                return False
    for i in range(n):
        for j in range(n):
            if solution[i][j] != 0 and solution[i + k][j] != 0 and solution[i][j] == solution[i + k][j]:
                return False
    return True

def solve_superdoku(n, k):
    solution = [[0] * n for _ in range(n)]
    for i in range(k):
        for j in range(n):
            solution[i][j] = i + 1
    for i in range(n):
        for j in range(n):
            if solution[i][j] == 0:
                for num in range(1, n + 1):
                    if is_valid_solution(solution, n, k, i, j, num):
                        solution[i][j] = num
                        if solve_superdoku(n, k, solution):
                            return solution
                        solution[i][j] = 0
    return False

def main():
    n, k = map(int, input().split())
    solution = solve_superdoku(n, k)
    if solution:
        for row in solution:
            print(*row)
    else:
        print("no")

if __name__ == '__main__':
    main()

