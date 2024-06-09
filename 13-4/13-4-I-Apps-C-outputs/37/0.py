
def get_input():
    n = int(input())
    pairs = []
    for _ in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    return n, pairs

def generate_equations(n, pairs):
    equations = []
    for i in range(n):
        for op in ["+", "-", "*"]:
            equation = f"{pairs[i][0]} {op} {pairs[i][1]} = "
            result = eval(equation)
            if result not in equations:
                equations.append(equation + str(result))
                break
        else:
            return "impossible"
    return equations

def main():
    n, pairs = get_input()
    equations = generate_equations(n, pairs)
    print("\n".join(equations))

if __name__ == '__main__':
    main()

