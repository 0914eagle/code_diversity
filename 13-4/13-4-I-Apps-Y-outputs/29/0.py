
def calculate_result(a, operation, b):
    if operation == '+':
        return a + b
    elif operation == '*':
        return a * b
    else:
        raise ValueError("Invalid operation")

def main():
    a = int(input())
    operation = input()
    b = int(input())
    result = calculate_result(a, operation, b)
    print(result)

if __name__ == '__main__':
    main()

