
def get_input():
    a = int(input())
    op = input()
    b = int(input())
    return a, op, b

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Invalid operation")

def main():
    a, op, b = get_input()
    result = calculate(a, op, b)
    print(result)

if __name__ == '__main__':
    main()

