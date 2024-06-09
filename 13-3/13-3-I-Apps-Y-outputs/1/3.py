
def lucas_sequence(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_sequence(n-1) + lucas_sequence(n-2)

def main():
    n = int(input())
    print(lucas_sequence(n))

if __name__ == '__main__':
    main()

