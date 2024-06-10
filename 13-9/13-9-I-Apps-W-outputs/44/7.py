
def get_numbers():
    a = float(input())
    b = float(input())
    return a, b

def get_operator():
    return input()

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a / b

def main():
    a, b = get_numbers()
    op = get_operator()
    print(calculate(a, b, op))

if __name__ == '__main__':
    main()

