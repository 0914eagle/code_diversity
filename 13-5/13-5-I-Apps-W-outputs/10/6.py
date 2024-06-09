
def is_solution(a, b, x):
    return a % x == b

def count_solutions(a, b):
    count = 0
    for x in range(1, b + 1):
        if is_solution(a, b, x):
            count += 1
    return count

def main():
    a, b = map(int, input().split())
    solutions = count_solutions(a, b)
    if solutions == float('inf'):
        print("infinity")
    else:
        print(solutions)

if __name__ == '__main__':
    main()

