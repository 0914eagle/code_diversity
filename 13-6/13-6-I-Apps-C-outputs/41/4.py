
def get_lawn_widths(n, s_list, g_list):
    s_list = [int(i) for i in s_list]
    g_list = [int(i) for i in g_list]
    total_lawn_width = sum(g_list)
    s_prime_list = []
    for i in range(n):
        s_prime = s_list[i] + g_list[i]
        s_prime_list.append(s_prime)
    for i in range(n-1):
        if abs(s_prime_list[i] - s_prime_list[i+1]) > 1:
            return -1
    return total_lawn_width, s_prime_list

def main():
    n = int(input())
    s_list = input().split()
    g_list = input().split()
    total_lawn_width, s_prime_list = get_lawn_widths(n, s_list, g_list)
    print(total_lawn_width)
    print(*s_prime_list)

if __name__ == '__main__':
    main()

