
def calculate_expression(n):
    return (1 ** n + 2 ** n + 3 ** n + 4 ** n) % 5

def input_data():
    n = int(input())
    return n

def main():
    n = input_data()
    result = calculate_expression(n)
    print(result)

if __name__ == '__main__':
    main()

