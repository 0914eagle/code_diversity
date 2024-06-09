
def number_of_digits(n):
    return len(str(n))

def label_books(n):
    return number_of_digits(n)

if __name__ == '__main__':
    n = int(input())
    print(label_books(n))

