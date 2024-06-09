
def get_input():
    return list(map(int, input().split()))

def reconstruct_equation(numbers):
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 == num3:
                    return f"{num1}+{num2}={num3}"
                elif num1 - num2 == num3:
                    return f"{num1}-{num2}={num3}"
                elif num1 * num2 == num3:
                    return f"{num1}*{num2}={num3}"
                elif num1 / num2 == num3:
                    return f"{num1}/{num2}={num3}"
    return "No solution found"

def main():
    numbers = get_input()
    equation = reconstruct_equation(numbers)
    print(equation)

if __name__ == '__main__':
    main()

