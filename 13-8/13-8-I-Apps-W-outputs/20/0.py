
def get_kth_digit(k):
    if k < 1:
        return -1
    n = 1
    while True:
        n += 1
        if len(str(n)) >= k:
            return int(str(n)[k-1])
def main():
    k = int(input())
    print(get_kth_digit(k))
if __name__ == '__main__':
    main()

