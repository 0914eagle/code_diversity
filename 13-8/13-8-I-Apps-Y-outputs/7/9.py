
def input_data():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def multiply(a):
    result = 1
    for i in range(len(a)):
        result *= a[i]
    return result

def main():
    n, a = input_data()
    result = multiply(a)
    if result > 10**18:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    main()

