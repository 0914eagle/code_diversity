
def get_solutions(a, b):
    solutions = []
    for x in range(1, b+1):
        if a % x == b:
            solutions.append(x)
    return solutions

def main():
    a, b = map(int, input().split())
    solutions = get_solutions(a, b)
    if len(solutions) == 0:
        print("infinity")
    else:
        print(len(solutions))

if __name__ == '__main__':
    main()

