
def get_input():
    A = int(input())
    operation = input()
    B = int(input())
    return A, operation, B

def calculate_result(A, operation, B):
    if operation == '+':
        return A + B
    elif operation == '*':
        return A * B
    else:
        raise ValueError("Invalid operation")

def main():
    A, operation, B = get_input()
    result = calculate_result(A, operation, B)
    print(result)

if __name__ == '__main__':
    main()

