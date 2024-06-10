
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:
        return a / b

def main():
    a = float(input())
    b = float(input())
    operator = input()
    result = calculate(a, b, operator)
    print(result)

if __name__ == '__main__':
    main()

