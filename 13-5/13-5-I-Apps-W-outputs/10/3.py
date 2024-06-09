
def modular_equation_solver(a, b):
    solutions = []
    for x in range(1, b+1):
        if a % x == b:
            solutions.append(x)
    if len(solutions) == 0:
        return "infinity"
    else:
        return len(solutions)

def main():
    a, b = map(int, input().split())
    print(modular_equation_solver(a, b))

if __name__ == '__main__':
    main()

