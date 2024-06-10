
def get_numbers():
    a = float(input())
    b = float(input())
    return a, b

def get_operator():
    return input()

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b

def main():
    a, b = get_numbers()
    operator = get_operator()
    result = calculate(a, b, operator)
    print(result)

if __name__ == '__main__':
    main()

