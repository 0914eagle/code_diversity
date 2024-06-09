
def calculate_expression(n):
    return (1**n + 2**n + 3**n + 4**n) % 5

def main():
    n = int(input())
    print(calculate_expression(n))

if __name__ == '__main__':
    main()

