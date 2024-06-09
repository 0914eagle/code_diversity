
def get_greek_numbers(n):
    return sum(int(i) for i in str(n))

def main():
    n = int(input())
    print(get_greek_numbers(n))

if __name__ == '__main__':
    main()

