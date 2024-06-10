
def get_input():
    return list(map(int, input().split()))

def get_equation(numbers):
    num1, num2, num3 = numbers
    for operation in "+-*/":
        for i in range(4):
            if eval(f"{num1}{operation}{num2}{operation}{num3}") == num1:
                return f"{num1}{operation}{num2}{operation}{num3}"

def main():
    numbers = get_input()
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

