
def get_equation(numbers):
    # Convert the list of numbers to a set to remove duplicates
    numbers = set(numbers)
    # Iterate over the possible operations
    for operation in ["+", "-", "*", "/"]:
        # Iterate over the possible combinations of numbers and operation
        for num1 in numbers:
            for num2 in numbers:
                if num1 != num2:
                    result = eval(str(num1) + operation + str(num2))
                    if result in numbers:
                        return str(num1) + operation + str(num2) + "=" + str(result)
    return "No solution found"

def main():
    numbers = [int(x) for x in input().split()]
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

