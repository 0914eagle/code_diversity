
def get_number_of_digits(n):
    return len(str(n))

def get_number_of_books(n):
    return n

def get_total_number_of_digits(n):
    return get_number_of_digits(get_number_of_books(n))

if __name__ == '__main__':
    n = int(input())
    print(get_total_number_of_digits(n))

