
def calculate_expression(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % 5
    return result

def main():
    n = int(input())
    print(calculate_expression(n))

if __name__ == '__main__':
    main()

