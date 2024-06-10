
def get_possible_solutions(b, d, c, l):
    solutions = []
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j + k == l and i * b + j * d + k * c == l:
                    solutions.append([i, j, k])
    return solutions

def print_solutions(solutions):
    if len(solutions) == 0:
        print("impossible")
    else:
        for solution in solutions:
            print(solution[0], solution[1], solution[2])

def main():
    b, d, c, l = map(int, input().split())
    solutions = get_possible_solutions(b, d, c, l)
    print_solutions(solutions)

if __name__ == '__main__':
    main()

