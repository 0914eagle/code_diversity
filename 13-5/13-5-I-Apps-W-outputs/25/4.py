
def get_least_number_of_digits_1(n):
    count = 0
    while n > 0:
        count += 1
        n -= pow(10, count - 1)
    return count

def main():
    n = int(input())
    print(get_least_number_of_digits_1(n))

if __name__ == '__main__':
    main()

