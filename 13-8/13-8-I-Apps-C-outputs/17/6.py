
def get_solution(n, vertical_spec, horizontal_spec):
    # Initialize the solution matrix
    solution = [[0] * (n+1) for _ in range(n)]

    # Fill in the vertical bars
    for i in range(n):
        for j in range(n+1):
            if vertical_spec[i][j] == 1:
                solution[i][j] = 1

    # Fill in the horizontal bars
    for i in range(n+1):
        for j in range(n):
            if horizontal_spec[i][j] == 1:
                solution[i][j] = 1

    return solution

def main():
    n = int(input())
    vertical_spec = []
    horizontal_spec = []
    for i in range(n):
        row = list(map(int, input().split()))
        vertical_spec.append(row)
    for i in range(n+1):
        col = list(map(int, input().split()))
        horizontal_spec.append(col)
    solution = get_solution(n, vertical_spec, horizontal_spec)
    for row in solution:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()

