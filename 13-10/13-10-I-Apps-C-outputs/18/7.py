
def get_remainder(x, y):
    return x % y

def get_ancient_remainders(c_list, k):
    return [get_remainder(c, k) for c in c_list]

def has_winning_strategy(n, k, c_list):
    ancient_remainders = get_ancient_remainders(c_list, k)
    if k in ancient_remainders:
        return True
    for i in range(n):
        if get_remainder(c_list[i], k) != ancient_remainders[i]:
            return False
    return True

def main():
    n, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    print("Yes") if has_winning_strategy(n, k, c_list) else print("No")

if __name__ == '__main__':
    main()

