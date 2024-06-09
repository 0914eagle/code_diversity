
def read_input():
    A = int(input())
    operation = input()
    B = int(input())
    return A, operation, B

def calculate_result(A, operation, B):
    if operation == '+':
        result = A + B
    elif operation == '*':
        result = A * B
    return result

def print_result(result):
    print(result)

if __name__ == '__main__':
    A, operation, B = read_input()
    result = calculate_result(A, operation, B)
    print_result(result)

