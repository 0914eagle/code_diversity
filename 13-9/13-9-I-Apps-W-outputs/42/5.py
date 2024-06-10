
def evaluate_expression(a, b):
    return (1**b + 2**b + ... + a**b) % a

def main():
    a, b = map(int, input().split())
    print(evaluate_expression(a, b))

if __name__ == '__main__':
    main()

