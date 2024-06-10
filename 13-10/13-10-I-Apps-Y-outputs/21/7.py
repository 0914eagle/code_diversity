
def number_of_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def main():
    n = int(input("Enter a binary string: "))
    print(number_of_ones(n))

if __name__ == '__main__':
    main()

