
def multiply(a, b):
    if a in range(1, 10) and b in range(1, 10):
        return a * b
    else:
        return -1

def main():
    a, b = map(int, input().split())
    result = multiply(a, b)
    print(result)

if __name__ == '__main__':
    main()

