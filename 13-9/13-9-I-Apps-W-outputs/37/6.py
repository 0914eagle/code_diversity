
def get_last_digit(n):
    return int(str(1378**n)[-1])

def main():
    n = int(input())
    print(get_last_digit(n))

if __name__ == '__main__':
    main()

