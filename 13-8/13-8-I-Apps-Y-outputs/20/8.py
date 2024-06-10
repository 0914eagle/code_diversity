
def get_inner_rating(N, R):
    if N >= 10:
        return R
    else:
        return R + 100 * (10 - N)

def main():
    N, R = map(int, input().split())
    print(get_inner_rating(N, R))

if __name__ == '__main__':
    main()

