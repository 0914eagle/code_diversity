
def read_input():
    return map(int, input().split())

def evaluate_expression(a, b):
    return sum(i ** b for i in range(1, a + 1)) % a

def main():
    a, b = read_input()
    print(evaluate_expression(a, b))

if __name__ == '__main__':
    main()

