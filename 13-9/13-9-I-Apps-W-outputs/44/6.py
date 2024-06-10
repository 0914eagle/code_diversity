
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
    print(calculate(a, b, c))

if __name__ == '__main__':
    main()

