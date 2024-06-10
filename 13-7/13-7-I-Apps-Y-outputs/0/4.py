
def get_possible_solutions(b, d, c, l):
    solutions = []
    for i in range(1, min(b, d, c) + 1):
        for j in range(1, min(b, d, c) + 1):
            for k in range(1, min(b, d, c) + 1):
                if i + j + k == l and i * b + j * d + k * c == 14:
                    solutions.append([i, j, k])
    return solutions

def print_solutions(solutions):
    if len(solutions) == 0:
        print("impossible")
    else:
        for solution in solutions:
            print(f"{solution[0]} {solution[1]} {solution[2]}")

if __name__ == '__main__':
    b, d, c, l = map(int, input().split())
    solutions = get_possible_solutions(b, d, c, l)
    print_solutions(solutions)

