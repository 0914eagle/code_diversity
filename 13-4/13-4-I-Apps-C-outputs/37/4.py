
def get_input():
    n = int(input())
    pairs = []
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    return n, pairs

def generate_equations(n, pairs):
    equations = []
    for i in range(n):
        a, b = pairs[i]
        if a + b != 0:
            equations.append(f"{a} + {b} = {a + b}")
        elif a - b != 0:
            equations.append(f"{a} - {b} = {a - b}")
        elif a * b != 0:
            equations.append(f"{a} * {b} = {a * b}")
        else:
            return "impossible"
    return equations

def main():
    n, pairs = get_input()
    equations = generate_equations(n, pairs)
    for equation in equations:
        print(equation)

if __name__ == '__main__':
    main()

