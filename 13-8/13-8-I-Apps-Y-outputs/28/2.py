
def get_equation(numbers):
    num1, num2, num3 = numbers
    for operation in "+-*/":
        for result in (num1, num2, num3):
            for num in (num1, num2, num3):
                if eval(f"{num}{operation}{result}") == num3:
                    return f"{num1}{operation}{result}={num3}"

def main():
    numbers = list(map(int, input().split()))
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

