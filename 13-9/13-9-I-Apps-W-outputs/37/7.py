
def get_last_digit(n):
    result = 1
    for i in range(n):
        result = (result * 1378) % 10
    return result

def main():
    n = int(input())
    print(get_last_digit(n))

if __name__ == '__main__':
    main()

