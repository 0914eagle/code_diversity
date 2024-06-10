
def get_input():
    return list(map(int, input().split()))

def reconstruct_equation(numbers):
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 == num3:
                    return str(num1) + "+" + str(num2) + "=" + str(num3)
                elif num1 - num2 == num3:
                    return str(num1) + "-" + str(num2) + "=" + str(num3)
                elif num1 * num2 == num3:
                    return str(num1) + "*" + str(num2) + "=" + str(num3)
                elif num1 / num2 == num3:
                    return str(num1) + "/" + str(num2) + "=" + str(num3)

def main():
    numbers = get_input()
    print(reconstruct_equation(numbers))

if __name__ == '__main__':
    main()

