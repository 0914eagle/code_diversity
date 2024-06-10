
def get_operator(c):
    if c == "+":
        return "+"
    elif c == "-":
        return "-"
    elif c == "*":
        return "*"
    else:
        return "/"

def calculate(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    else:
        return a / b

def main():
    a = float(input())
    b = float(input())
    c = input()
    operator = get_operator(c)
    result = calculate(a, b, operator)
    print(result)

if __name__ == '__main__':
    main()

