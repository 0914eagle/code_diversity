
def get_remainder(x, k):
    return x % k

def get_winning_strategy(n, k, c):
    if k in c:
        return "Yes"
    else:
        return "No"

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    print(get_winning_strategy(n, k, c))

if __name__ == '__main__':
    main()

