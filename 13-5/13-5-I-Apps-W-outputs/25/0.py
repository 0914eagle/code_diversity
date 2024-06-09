
def get_digits_1(n):
    return len(str(bin(n)[2:]))

def get_least_number_of_digits_1(n):
    digits_1 = get_digits_1(n)
    for i in range(1, n):
        if get_digits_1(i) < digits_1:
            digits_1 = get_digits_1(i)
    return digits_1

if __name__ == '__main__':
    n = int(input())
    print(get_least_number_of_digits_1(n))

