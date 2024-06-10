
def get_inner_rating(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

def main():
    n, r = map(int, input().split())
    print(get_inner_rating(n, r))

if __name__ == '__main__':
    main()

