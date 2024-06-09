
def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_number(n-1) + lucas_number(n-2)

def main():
    n = int(input())
    print(lucas_number(n))

if __name__ == '__main__':
    main()

