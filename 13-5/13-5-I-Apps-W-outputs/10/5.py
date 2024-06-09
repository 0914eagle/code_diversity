
def is_solution(a, b, x):
    return a % x == b

def count_solutions(a, b):
    solutions = 0
    for x in range(1, b+1):
        if is_solution(a, b, x):
            solutions += 1
    return solutions

def main():
    a, b = map(int, input().split())
    solutions = count_solutions(a, b)
    if solutions == float('inf'):
        print("infinity")
    else:
        print(solutions)

if __name__ == '__main__':
    main()

