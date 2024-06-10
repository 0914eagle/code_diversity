
def get_digit(k):
    if k == 1:
        return 1
    else:
        return (k * (k + 1)) % 10

def main():
    k = int(input())
    print(get_digit(k))

if __name__ == '__main__':
    main()

