
def get_numbers():
    A = float(input())
    B = float(input())
    return A, B

def get_operator():
    return input()

def calculate(A, B, operator):
    if operator == "+":
        return A + B
    elif operator == "-":
        return A - B
    elif operator == "*":
        return A * B
    else:
        return A / B

def main():
    A, B = get_numbers()
    operator = get_operator()
    print(calculate(A, B, operator))

if __name__ == '__main__':
    main()

