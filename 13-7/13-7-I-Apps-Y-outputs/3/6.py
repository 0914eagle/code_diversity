
def get_number_of_digits(n):
    return len(str(n))

def get_odd_numbers_less_than_or_equal_to(n):
    count = 0
    for i in range(1, n+1):
        if get_number_of_digits(i) % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(get_odd_numbers_less_than_or_equal_to(n))

