
def get_number_of_digits(n):
    return len(str(n))

def get_label_for_book(n):
    return get_number_of_digits(n)

def get_total_number_of_digits(n):
    return sum(get_label_for_book(i) for i in range(1, n + 1))

if __name__ == '__main__':
    n = int(input())
    print(get_total_number_of_digits(n))

