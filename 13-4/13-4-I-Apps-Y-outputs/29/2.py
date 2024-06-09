
def calculate_result(a, operation, b):
    if operation == '+':
        return a + b
    elif operation == '*':
        return a * b
    else:
        raise ValueError("Invalid operation")

def get_input():
    a = int(input("Enter the first operand: "))
    operation = input("Enter the operation (+ or *): ")
    b = int(input("Enter the second operand: "))
    return a, operation, b

def main():
    a, operation, b = get_input()
    result = calculate_result(a, operation, b)
    print(f"The result is: {result}")

if __name__ == '__main__':
    main()

