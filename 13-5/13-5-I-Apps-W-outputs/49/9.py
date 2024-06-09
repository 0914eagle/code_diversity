
def get_arithmetic_progression(n, a):
    # Calculate the common difference of the arithmetic progression
    common_diff = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] != common_diff:
            return -1
    return common_diff

def get_possible_values(n, a, common_diff):
    # Calculate the first term of the arithmetic progression
    first_term = a[0]
    for i in range(1, n):
        first_term += common_diff
        if first_term > 10**8:
            return -1
    return first_term

def main():
    n = int(input())
    a = list(map(int, input().split()))
    common_diff = get_arithmetic_progression(n, a)
    if common_diff == -1:
        print(-1)
    else:
        first_term = get_possible_values(n, a, common_diff)
        if first_term == -1:
            print(-1)
        else:
            print(len(set(a)))
            print(*sorted(set(a)), sep='\n')

if __name__ == '__main__':
    main()

