
def get_input():
    return [int(x) for x in input().split()]

def get_equation(numbers):
    a, b, c = numbers
    for operation in ['+', '-', '*', '/']:
        if eval(f'{a}{operation}{b}') == c:
            return f'{a} {operation} {b} = {c}'

def main():
    numbers = get_input()
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

