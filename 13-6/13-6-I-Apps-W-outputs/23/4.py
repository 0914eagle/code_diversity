
def calculate_expression(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**n
    return sum % 5

def main():
    n = int(input())
    print(calculate_expression(n))

if __name__ == '__main__':
    main()

