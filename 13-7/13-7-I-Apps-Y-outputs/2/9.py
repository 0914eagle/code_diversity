
def is_divisible_by_25(n):
    while n % 25 != 0:
        n = int(str(n)[:-1] + str(n)[1:])
    return n

def get_min_moves(n):
    count = 0
    while n % 25 != 0:
        n = int(str(n)[:-1] + str(n)[1:])
        count += 1
    return count

def main():
    n = int(input())
    print(get_min_moves(n))

if __name__ == '__main__':
    main()

