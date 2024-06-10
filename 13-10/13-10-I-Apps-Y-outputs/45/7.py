
def get_input():
    return list(map(int, input().split()))

def solve(p_list):
    N = len(p_list)
    max_price = max(p_list)
    total = sum(p_list)
    for i in range(N):
        if p_list[i] == max_price:
            total -= max_price // 2
            break
    return total

def main():
    p_list = get_input()
    print(solve(p_list))

if __name__ == '__main__':
    main()

