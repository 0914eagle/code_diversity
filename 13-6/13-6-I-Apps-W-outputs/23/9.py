
def calculate_expression(n):
    result = 1
    for i in range(1, n+1):
        result += i**n
    return result % 5

def main():
    n = int(input())
    print(calculate_expression(n))

if __name__ == '__main__':
    main()

