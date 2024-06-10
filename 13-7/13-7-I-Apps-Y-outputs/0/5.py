
def find_solutions(b, d, c, l):
    solutions = []
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j + k == l and b*i + d*j + c*k == 14:
                    solutions.append([i, j, k])
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print(solution[0], solution[1], solution[2])

if __name__ == '__main__':
    b, d, c, l = map(int, input().split())
    solutions = find_solutions(b, d, c, l)
    print_solutions(solutions)

