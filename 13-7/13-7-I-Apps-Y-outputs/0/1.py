
def solve(b, d, c, l):
    solutions = []
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j + k == l and i * b + j * d + k * c == 14:
                    solutions.append([i, j, k])
    return solutions

def main():
    b, d, c, l = map(int, input().split())
    solutions = solve(b, d, c, l)
    if len(solutions) == 0:
        print("impossible")
    else:
        for solution in solutions:
            print(" ".join(map(str, solution)))

if __name__ == '__main__':
    main()

