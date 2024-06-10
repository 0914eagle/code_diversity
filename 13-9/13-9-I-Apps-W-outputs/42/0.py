
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += i**b
    return result % a

def main():
    a, b = map(int, input().split())
    print(evaluate_expression(a, b))

if __name__ == '__main__':
    main()

