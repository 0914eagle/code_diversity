
def get_remainders(x, c_list):
    return [x % c for c in c_list]

def has_winning_strategy(k, c_list):
    if k in c_list:
        return True
    else:
        return False

def main():
    n, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    remainders = get_remainders(k, c_list)
    print("Yes") if has_winning_strategy(k, c_list) else print("No")

if __name__ == '__main__':
    main()

