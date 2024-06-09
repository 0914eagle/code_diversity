
def can_multiply(a, b):
    return 1 <= a <= 9 and 1 <= b <= 9

def multiply(a, b):
    if can_multiply(a, b):
        return a * b
    else:
        return -1

def main():
    a, b = map(int, input().split())
    result = multiply(a, b)
    print(result)

if __name__ == '__main__':
    main()

