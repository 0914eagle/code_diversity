
def get_k_rounding(n, k):
    if k == 0:
        return n
    else:
        return n * 10 ** k

def main():
    n, k = map(int, input().split())
    print(get_k_rounding(n, k))

if __name__ == '__main__':
    main()

