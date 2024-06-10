
def get_last_digit_of_power(n):
    return str(1378**n)[-1]

def main():
    n = int(input())
    print(get_last_digit_of_power(n))

if __name__ == '__main__':
    main()

