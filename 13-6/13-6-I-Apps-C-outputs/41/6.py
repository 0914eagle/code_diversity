
def get_lawn_widths(n, s_list, g_list):
    total_lawn_width = 0
    s_prime_list = []
    for i in range(n):
        s_prime = s_list[i] + g_list[i]
        g_prime = g_list[i] - s_list[i]
        total_lawn_width += g_prime
        s_prime_list.append(s_prime)
    return total_lawn_width, s_prime_list

def get_solution(n, s_list, g_list):
    total_lawn_width, s_prime_list = get_lawn_widths(n, s_list, g_list)
    for i in range(n-1):
        if abs(s_prime_list[i] + 1 - s_prime_list[i+1]) > 1:
            return -1
    return total_lawn_width, s_prime_list

if __name__ == '__main__':
    n = int(input())
    s_list = []
    g_list = []
    for i in range(n):
        s, g = map(int, input().split())
        s_list.append(s)
        g_list.append(g)
    total_lawn_width, s_prime_list = get_solution(n, s_list, g_list)
    print(total_lawn_width)
    print(*s_prime_list)

