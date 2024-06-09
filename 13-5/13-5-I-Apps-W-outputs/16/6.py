
def get_number_of_digits(n):
    return len(str(n))

def get_number_of_books(n):
    return n

def get_total_number_of_digits(n):
    return sum(get_number_of_digits(i) for i in range(1, get_number_of_books(n) + 1))

if __name__ == '__main__':
    n = int(input())
    print(get_total_number_of_digits(n))

